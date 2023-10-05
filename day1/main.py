from dataclasses import dataclass

@dataclass
class Point:
       x: int
       y: int

p = Point(x=10, y=20)
q = Point(x=10, y=20)

print(p.z)
print(p == q)
