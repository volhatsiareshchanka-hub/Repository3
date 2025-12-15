# 1.	Свойства (@property); 1.1. Валидация через setter

class Product:
    def __init__(self, price):
        self._price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            print("Negative price is not allowed!")
        else:
            self._price = value


p = Product(100)
print(p.price)   # 100
p.price = 250
print(p.price)   # 250
p.price = -10  # Отрицательную цену задать нельзя
print(p.price)   # 250




