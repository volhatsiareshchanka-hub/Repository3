# 5.2. Длительность теста с арифметикой (__add__, __str__)

class Duration:
    def __init__(self, duration):
        self.duration = duration

    def __add__(self, other):
        return Duration(self.duration + other.duration)

    def __str__(self):
        return str(f"{self.duration:.2f} sec")

d1 = Duration(1.5)
d2 = Duration(2.7)
d3 = d1 + d2

print(d1)  # 1.50 sec
print(d2)  # 2.70 sec
print(d3)  # 4.20 sec
