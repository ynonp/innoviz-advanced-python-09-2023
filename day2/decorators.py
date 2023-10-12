def debug(f):
    def inner(*args, **kwargs):
        print(f"{f} was called with: {args} and {kwargs}")
        ret = f(*args, **kwargs)
        print(f"{f} has ended and returned {ret}")
        return ret
    return inner


def count(f):
    n = 0
    def inner(*args, **kwargs):
        nonlocal n
        n += 1
        print(f"Function {f} was called {n} times")
        ret = f(*args, **kwargs)
        return ret
    return inner



@count
def say_hi():
    print("hello world")


@count
def twice(x):
    return x * 2


say_hi()
say_hi()
say_hi()
print(twice(2))
print(twice(2))

