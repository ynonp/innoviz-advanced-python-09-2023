from typing import TypedDict

def longer_than(items: list[str], min_length: int) -> list[str]:
    return [i for i in items if len(i) > min_length]


print(longer_than(['one', 'two', 'three', 'four'], 3))
# print(longer_than([10, 20], 3))


class Point2D(TypedDict):
   x: int
   y: int

def print_x(p: Point2D) -> None:
    print(p["x"])


print_x({"x": 10, "y": 20})
print_x({"X": 10, "Y": 20})

