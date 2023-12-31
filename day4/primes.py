"""
Count prime numbers from threads
"""
import math
import threading
import cProfile
primes_count = 0

lock = threading.Lock()

# GIL


def is_prime(n: int):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def primes_in_range(start: int, end: int):
    global primes_count
    result = sum([is_prime(i) for i in range(start, end)])
    with lock:
        primes_count += result


# Exercise: split this work to multiple threads, and see if you can
# make the calculation faster
def without_threads():
    global primes_count
    primes_count = 0

    primes_in_range(2, 1_000_000)
    print(primes_count)


def with_threads():
    global primes_count
    primes_count = 0
    t1 = threading.Thread(target=primes_in_range, args=(2, 500_000))
    t2 = threading.Thread(target=primes_in_range, args=(500_000, 1_000_000))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print(primes_count)


if __name__ == "__main__":
    cProfile.run("with_threads()")
    # cProfile.run("without_threads()")
