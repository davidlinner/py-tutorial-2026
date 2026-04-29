"""
Process-pool demo: run CPU-heavy tasks in parallel using separate processes.

Learning goal: threads in Python share one CPU core for compute work due to
the GIL. Separate processes each get their own core, so CPU-bound work
genuinely runs in parallel.

Use this model for independent, CPU-heavy tasks such as image processing,
numerical computation, or repeated hashing.
"""

import concurrent.futures
import time


def count_primes(limit: int) -> int:
    """Count prime numbers up to `limit` using trial division."""
    count = 0
    for n in range(2, limit):
        if all(n % i != 0 for i in range(2, int(n**0.5) + 1)):
            count += 1
    return count


def main() -> None:
    # Each range is an independent CPU-heavy unit of work.
    ranges = [50_000, 60_000, 55_000, 45_000, 52_000]

    print("Counting primes sequentially first ...\n")
    start = time.perf_counter()
    sequential_results = [count_primes(limit) for limit in ranges]
    sequential_time = time.perf_counter() - start
    print(f"Sequential results : {sequential_results}")
    print(f"Sequential time    : {sequential_time:.2f}s\n")

    print("Now counting primes with ProcessPoolExecutor ...\n")
    start = time.perf_counter()
    with concurrent.futures.ProcessPoolExecutor() as executor:
        # map() distributes the work across processes and collects results in order.
        parallel_results = list(executor.map(count_primes, ranges))
    parallel_time = time.perf_counter() - start
    print(f"Parallel results   : {parallel_results}")
    print(f"Parallel time      : {parallel_time:.2f}s")
    print(f"Speedup            : {sequential_time / parallel_time:.1f}x")


# ProcessPoolExecutor requires this guard on Windows.
if __name__ == "__main__":
    main()
