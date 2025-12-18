# Class-based декоратор для добавления тэга

class Tag_name:
    def __init__(self, tag):
        self.tag = tag

    def __call__(self, cls):
        cls.tag = self.tag
        return cls

@Tag_name("smoke")
class SmokeTests:
    pass

@Tag_name("regression")
class RegressionTests:
    pass

print(SmokeTests.tag)       # smoke
print(RegressionTests.tag)  # regression
