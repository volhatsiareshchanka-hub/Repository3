# 9. Точка на плоскости

from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float


p1 = Point(1.0, 2.0)
p2 = Point(-3.5, 4.2)

print(p1)  # Point(x=1.0, y=2.0)
print(p2)  # Point(x=-3.5, y=4.2)

