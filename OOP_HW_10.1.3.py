# 1.3. Свойство для процента выполнения тестов

class TestStats:
    def __init__(self, passed, total):
        self.passed = passed
        self.total = total

    @property
    def success_rate(self):
        return (self.passed / self.total) * 100


stats = TestStats(8, 10)
print(stats.success_rate)   # 80.0
stats.passed = 9
print(stats.success_rate)   # 90.0
