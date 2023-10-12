import itertools

def fib():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


def even_numbers():
    n = 0
    while True:
        yield n
        n += 2


for i in even_numbers():
    if i > 100:
        print(i)
        break


print(list(itertools.islice(even_numbers(), 10)))
print(sum(itertools.islice(even_numbers(), 10)))

print(list(itertools.islice(fib(), 10)))
print(sum(itertools.islice(fib(), 10)))

for i in fib():
    print(i)
    if i > 100:
        break










