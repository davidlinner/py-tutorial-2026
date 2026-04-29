"""
Thread shared-state demo: two patterns for coordinating threads.

Pattern A — threading.Lock around a shared counter.
Pattern B — queue.Queue for producer/consumer communication.

Learning goal: threads share memory, which is convenient but risky.
Without a lock, concurrent writes corrupt the counter.
A Queue is often safer because it transfers ownership of data rather
than sharing a mutable variable.
"""

import queue
import threading
import time


# ── Pattern A: shared counter protected by a Lock ────────────────────────────

def increment_worker(counter: list, lock: threading.Lock, n: int) -> None:
    """Increment a shared counter n times, protected by a lock."""
    for _ in range(n):
        with lock:
            counter[0] += 1  # only one thread enters this block at a time


def demo_lock() -> None:
    print("Pattern A: shared counter with threading.Lock")
    counter = [0]  # list so the integer is mutable from worker threads
    lock = threading.Lock()
    threads = [
        threading.Thread(target=increment_worker, args=(counter, lock, 1000))
        for _ in range(5)
    ]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    print(f"  Expected: 5000  Got: {counter[0]}")
    print()


# ── Pattern B: producer/consumer with queue.Queue ─────────────────────────────

SENTINEL = None  # signal that the producer is done


def producer(q: queue.Queue, items: list) -> None:
    for item in items:
        time.sleep(0.05)  # simulate work between items
        q.put(item)
        print(f"  produced: {item}")
    q.put(SENTINEL)  # tell the consumer there is nothing more


def consumer(q: queue.Queue) -> None:
    while True:
        item = q.get()
        if item is SENTINEL:
            break
        print(f"  consumed: {item}")
        q.task_done()


def demo_queue() -> None:
    print("Pattern B: producer/consumer with queue.Queue")
    q: queue.Queue = queue.Queue(maxsize=3)  # buffer at most 3 items
    items = ["alpha", "beta", "gamma", "delta", "epsilon"]

    p = threading.Thread(target=producer, args=(q, items))
    c = threading.Thread(target=consumer, args=(q,))

    p.start()
    c.start()
    p.join()
    c.join()
    print()


if __name__ == "__main__":
    demo_lock()
    demo_queue()
