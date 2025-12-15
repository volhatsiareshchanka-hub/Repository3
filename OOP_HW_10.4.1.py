# Полиморфизм; 4.1. Полиморфные тесты (API и UI)

class BaseTest:
    def run(self):
        pass

class APITest(BaseTest):
    def __init__(self, endpoint):
        self.endpoint = endpoint
    def run(self):
        print(f"API Test(проверяем эндпоинт /login")

class UITest(BaseTest):
    def __init__(self, page):
        self.page = page
    def run(self):
        print(f"UI тест: проверяем страницу LoginPage")

def run_all(tests):
    for test in tests:
        test.run()

tests = [
    APITest("/login"),
    UITest("LoginPage"),
    APITest("/users"),
]
run_all(tests)

# API тест: проверяем эндпоинт /login
# UI тест: проверяем страницу LoginPage
# API тест: проверяем эндпоинт /users



