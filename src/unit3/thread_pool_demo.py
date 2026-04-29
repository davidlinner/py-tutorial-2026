"""
Thread-pool demo: run blocking functions concurrently using threads.

Learning goal: when you have a blocking synchronous function (e.g. from a
library that has no async version), a thread pool lets multiple calls
overlap even though each call blocks its own thread.

Use this model when you cannot use asyncio because the code you are calling
does not support `await`.
"""

import concurrent.futures
import time


def slow_blocking_task(name: str, duration: float) -> str:
    """Simulate a blocking library call (e.g. a synchronous HTTP client)."""
    print(f"  [{name}] starting  (will take {duration:.1f}s)")
    time.sleep(duration)  # blocking — cannot be awaited
    print(f"  [{name}] done")
    return f"{name} finished"


def main() -> None:
    tasks = [
        ("Task A", 1.0),
        ("Task B", 1.5),
        ("Task C", 0.8),
        ("Task D", 1.2),
        ("Task E", 0.5),
    ]

    print("Running tasks with ThreadPoolExecutor ...\n")
    start = time.perf_counter()

    # max_workers controls how many threads run at the same time.
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        # submit() schedules each call and returns a Future.
        futures = {
            executor.submit(slow_blocking_task, name, duration): name
            for name, duration in tasks
        }
        results = []
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())

    elapsed = time.perf_counter() - start
    print(f"\nAll done. Results: {results}")
    print(f"Total time: {elapsed:.2f}s")
    # Expected: close to the longest single duration (~1.5 s).


if __name__ == "__main__":
    main()
