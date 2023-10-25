import itertools


# prints: 1, 2, 3, 4, 5
# for item in uniq([1, 2, 2, 2, 3, 4, 5]):
#     print(item)



def digits(n: int):
    while n > 0:
        yield n % 10
        n //= 10


# print: 15
print(sum(digits(12345)))


def uniq_not_generator(items):
    for i in set(items):
        yield i


def uniq(sequence):
    """
    Create a generator named 'uniq' that returns only values it hasn't seen before
    (so if a value appears multiple times it will only be returned the first time we encounter it)
    """
    seen = set()
    for i in sequence:
        if i not in seen:
            yield i
        seen.add(i)


def even_numbers():
    n = 0
    while True:
        yield n
        n += 2


print(list(itertools.islice(even_numbers(), 10)))

# this works
print(list(itertools.islice(uniq(even_numbers()), 10)))

# this doesn't work
# print(list(itertools.islice(uniq_not_generator(even_numbers()), 10)))


