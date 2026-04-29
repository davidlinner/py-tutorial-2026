"""
Async I/O with timeouts and concurrency limits.

Learning goal: starting all tasks at once can overwhelm a remote service or
exceed rate limits. A Semaphore limits how many tasks are active at the same
time. asyncio.wait_for() cancels a task that takes too long.

Real-world analogy: a semaphore is like a ticket counter — only N callers
can be served simultaneously; the rest wait their turn.
"""

import asyncio
import random
import time


CONCURRENCY_LIMIT = 3  # at most this many tasks run at the same time
TIMEOUT_SECONDS = 2.0  # tasks slower than this are cancelled


async def api_call(name: str, semaphore: asyncio.Semaphore) -> str:
    """Simulate an API call with a random response time."""
    async with semaphore:
        # Random delay: some calls will exceed the timeout.
        delay = random.uniform(0.5, 3.0)
        print(f"  [{name}] started  (simulated delay {delay:.1f}s)")
        await asyncio.sleep(delay)
        print(f"  [{name}] done")
        return f"{name} ok"


async def safe_call(name: str, semaphore: asyncio.Semaphore) -> str:
    """Wrap api_call with a timeout so a slow call does not block the program."""
    try:
        result = await asyncio.wait_for(
            api_call(name, semaphore), timeout=TIMEOUT_SECONDS
        )
        return result
    except asyncio.TimeoutError:
        print(f"  [{name}] TIMED OUT after {TIMEOUT_SECONDS}s")
        return f"{name} timed out"


async def main() -> None:
    random.seed(42)
    task_names = [f"API-{i}" for i in range(1, 9)]

    semaphore = asyncio.Semaphore(CONCURRENCY_LIMIT)

    print(
        f"Running {len(task_names)} API calls "
        f"(limit={CONCURRENCY_LIMIT}, timeout={TIMEOUT_SECONDS}s) ...\n"
    )
    start = time.perf_counter()

    results = await asyncio.gather(
        *[safe_call(name, semaphore) for name in task_names]
    )

    elapsed = time.perf_counter() - start
    print(f"\nAll done. Results: {results}")
    print(f"Total time: {elapsed:.2f}s")


if __name__ == "__main__":
    asyncio.run(main())
