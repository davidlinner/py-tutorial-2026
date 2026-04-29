"""
Sequential baseline: each task runs one after the other.

Learning goal: sequential waiting is simple but may waste time when tasks
are independent. Compare the total runtime here to the asyncio and
thread-pool versions.
"""

import time


def slow_task(name: str, duration: float) -> str:
    """Simulate a slow operation (e.g. a network request or file read)."""
    print(f"  [{name}] starting  (will take {duration:.1f}s)")
    time.sleep(duration)
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

    print("Running tasks sequentially ...\n")
    start = time.perf_counter()

    results = [slow_task(name, duration) for name, duration in tasks]

    elapsed = time.perf_counter() - start
    print(f"\nAll done. Results: {results}")
    print(f"Total time: {elapsed:.2f}s")
    # Expected: roughly the sum of all durations (~5 s).


if __name__ == "__main__":
    main()