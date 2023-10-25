"""
Count prime numbers from threads
"""
import math
import multiprocessing
import cProfile
primes_count = 0

lock = multiprocessing.Lock()

# multiprocessing
# 1. Each task is executed in its own python interpreter (no GIL)
# 2. Each task (using its own interpreter) also has its own memory


def is_prime(n: int):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def primes_in_range(range_tuple):
    start, end = range_tuple
    return sum([is_prime(i) for i in range(start, end)])


# Exercise: split this work to multiple threads, and see if you can
# make the calculation faster
def without_threads():
    global primes_count
    primes_count = 0

    primes_in_range(2, 1_000_000)
    print(primes_count)


def with_threads():
    with multiprocessing.Pool(processes=4) as pool:
        # results = pool.map(primes_in_range, [(2, 500_000), (500_000, 1_000_000)])
        results = pool.map(is_prime, range(2, 1_000_000))
        print(sum(results))


if __name__ == "__main__":
    cProfile.run("with_threads()")
    # cProfile.run("without_threads()")
