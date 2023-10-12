from functools import partial

actions = {}

for idx, act in enumerate(['one', 'two', 'three', 'four']):
    # actions[act] = (lambda x: lambda: print(x))(idx)
    actions[act] = partial(lambda x: print(x), idx)

actions['one']()


