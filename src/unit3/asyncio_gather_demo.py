"""
Async I/O demo: many waiting tasks run concurrently on a single thread.

Learning goal: async tasks overlap during their waiting time.
asyncio.gather() starts all coroutines and lets them suspend at every
`await` so other coroutines can make progress.

Compare total runtime to sync_sleep_baseline.py — the time saved is the
time that was previously wasted waiting.
"""

import asyncio
import time


async def slow_task(name: str, duration: float) -> str:
    """Simulate a slow I/O operation (e.g. a network request)."""
    print(f"  [{name}] starting  (will take {duration:.1f}s)")
    # asyncio.sleep suspends this coroutine without blocking the event loop.
    await asyncio.sleep(duration)
    print(f"  [{name}] done")
    return f"{name} finished"


async def main() -> None:
    tasks = [
        ("Task A", 1.0),
        ("Task B", 1.5),
        ("Task C", 0.8),
        ("Task D", 1.2),
        ("Task E", 0.5),
    ]

    print("Running tasks with asyncio.gather() ...\n")
    start = time.perf_counter()

    # gather() starts all coroutines concurrently and waits for all of them.
    results = await asyncio.gather(
        *[slow_task(name, duration) for name, duration in tasks]
    )

    elapsed = time.perf_counter() - start
    print(f"\nAll done. Results: {results}")
    print(f"Total time: {elapsed:.2f}s")
    # Expected: roughly the longest single duration (~1.5 s), not the sum.


if __name__ == "__main__":
    asyncio.run(main())
