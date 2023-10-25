"""
Count prime numbers from threads
"""
import math

def is_prime(n: int):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


# Exercise: split this work to multiple threads, and see if you can
# make the calculation faster
print(sum([is_prime(i) for i in range(2, 1_000_000)]))
