# 6. Enum типов тестов и фильтрация

from enum import Enum

class TestType(Enum):
    API = 1
    UI = 2
    UNIT = 3

tests = [
        ("test_login_api", TestType.API),
        ("test_login_ui", TestType.UI),
        ("test_sum", TestType.UNIT),
        ("test_profile_api", TestType.API),
    ]

def filter_tests_by_type(tests, test_type: TestType):
    return [test for test in tests if test[1] == test_type]


# Проверка
print(filter_tests_by_type(tests, TestType.API))
print(filter_tests_by_type(tests, TestType.UI))
print(filter_tests_by_type(tests, TestType.UNIT))


