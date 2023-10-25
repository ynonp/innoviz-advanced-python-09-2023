import threading
total = 0
import cProfile

lock = threading.Lock()


def calculator(start: int, end: int):
    global total
    result = sum(range(start, end))
    with lock:
        total += result


def with_threads():
    t1 = threading.Thread(target=calculator, args=(1, 50_000_000))
    t2 = threading.Thread(target=calculator, args=(50_000_000, 100_000_000))

    t1.start()
    t2.start()

    # do something when both threads finished their work
    t1.join()
    t2.join()

    print(total)


def without_threads():
    print(sum(range(1, 100_000_000)))


if __name__ == "__main__":
    cProfile.run("without_threads()")
