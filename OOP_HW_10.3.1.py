# 3.	Абстракция; 3.1. Базовый абстрактный класс «Фигура»

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)


shapes = [Rectangle(3, 4), Circle(2)]
for s in shapes:
    if isinstance(s, Rectangle):
        print(f"Прямоугольник. Площадь {s.area():.2f}")
    if isinstance(s, Circle):
        print(f"Круг. Площадь: {s.area():.2f}")

# Прямоугольник. Площадь: 12
# Круг. Площадь: 12,57
