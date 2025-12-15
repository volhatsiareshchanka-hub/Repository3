# Магические методы; 5.1. Коллекция результатов как словарь (__getitem__, __setitem__, __len__)

class TestResults:
    def __init__(self):
        self.results = {}

    def __setitem__(self, key, value):
        self.results[key] = value

    def __getitem__(self, key):
        return self.results[key]

    def __len__(self):
        return len(self.results)


results = TestResults()
results["test_login"] = "passed"
results["test_payment"] = "failed"

print(results["test_login"])   # passed
print(len(results))            # 2
