# 1 1 2 3 5 8 13 21 34
def cached(f):
    def inner(*args, **kwargs):
        ret = f(*args, **kwargs)
        return ret
    return inner

@memoize
def fib(n):
    print(f"calculating fib({n})")
    if n < 2:
        return 1

    return fib(n-1) + fib(n-2)

# This line should print ONLY
# calculating fib(8)
# calculating fib(7)
# calculating fib(6)
# calculating fib(5)
# calculating fib(4)
# calculating fib(3)
# calculating fib(2)
# calculating fib(1)
# calculating fib(0)
print(fib(8))
