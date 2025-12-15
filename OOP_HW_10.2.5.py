# 2.5. Несколько миксинов

class LoggingMixin:
    def log(self):
        print("[LOG] Выполняем задачу")

class RetryMixin:
    def retry(self, attempts=2):
        for attempt in range(1, attempts + 1):
            print(f"Попытка {attempt}")
            self.log()
            print("Job что-то делает...")

class Job(LoggingMixin, RetryMixin):
    def run(self):
        self.retry()

j = Job()
j.retry(2)
# Попытка 1
# [LOG] Выполняем задачу
# Job что-то делает...
# Попытка 2
# [LOG] Выполняем задачу
# Job что-то делает...

