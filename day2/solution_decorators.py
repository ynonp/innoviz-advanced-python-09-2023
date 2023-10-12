def after5(f):
    counter = 0
    def inner(*args, **kwargs):
        nonlocal counter
        counter += 1
        if counter > 5:
            ret = f(*args, **kwargs)
            return ret
    return inner

@after5
def doit(): print("Yo!")

# ignore the first 5 calls
doit()
doit()
doit()
doit()
doit()

# so only print yo once
doit()



def accepts(*types):
    def decorator(f):
        def inner(*args, **kwargs):
            assert len(args) == len(types)
            for a, t in zip(args, types):
                assert type(a) == t
            ret = f(*args, **kwargs)
            return ret
        return inner

    return decorator

# make sure function can only be called with a float and an int
@accepts(float, int)
def pow(base, exp):
  pass

# raise AssertionError
pow(12.0, 10)