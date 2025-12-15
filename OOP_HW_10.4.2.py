# 4.2. Полиморфизм через утиный тип (без ABC)

class TestCollection:
    def __init__(self, tests):
        self.tests = tests

    def __len__(self):
        return len(self.tests)

def print_length(obj):
    print(len(obj))

print_length("Python") #6
print_length([1, 2, 3]) #3
print_length({"a": 1, "b": 2}) #2
print_length(TestCollection([10, 20, 30, 40])) #4

