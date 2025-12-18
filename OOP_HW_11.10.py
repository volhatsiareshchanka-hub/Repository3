# 10. Товар и общая стоимость

from dataclasses import dataclass

@dataclass
class Product:
    name: str
    price: float
    quantity: int

    def total(self):
        return self.price * self.quantity


p1 = Product("Keyboard", 50.0, 2)
p2 = Product("Mouse", 25.0, 4)  # added 4 as throwing error

print(p1, "total:", p1.total())  # 100.0
print(p2, "total:", p2.total())  # 25.0
