def uniq(sequence):
    """
    Create a generator named 'uniq' that returns only values it hasn't seen before
    (so if a value appears multiple times it will only be returned the first time we encounter it)
    """
    pass

# prints: 1, 2, 3, 4, 5
for item in uniq([1, 2, 2, 2, 3, 4, 5]):
    print(item)



def digits(n: int):
    """
    Create a generator that takes a number and yields the digits of that number
    :param n:
    """
    pass


# print: 15
print(sum(digits(12345)))
