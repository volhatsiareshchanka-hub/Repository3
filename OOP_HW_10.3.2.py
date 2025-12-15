# 3.2. Абстракция «Транспорт» с шаблонным методом

from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def move(self):
        pass
    def go(self):
        print("Начинаем движение")
        self.move()


class Car(Transport):
    def move(self):
        print("Едем по дороге на машине")


class Bike(Transport):
    def move(self):
        print("Едем на велосипеде")

transport =(Car(), Bike())
for t in (Car(), Bike()):
    t.go()
