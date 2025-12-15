# 2.2 Делегирование логгеру

class Logger:
    def log(self, message):
        print(f"[Log] {message}")

class Service:
    def __init__(self, logger):
        self.logger = logger  # Delegat
    def process(self):
        self.logger.log("Начал обработку")
        print("Обрабатываю")
        self.logger.log("Закончил обработку")


l = Logger()
s = Service(l)
s.process()
# [Log] Начал обработку
# Обрабатываю
# [Log] Закончил обработку
