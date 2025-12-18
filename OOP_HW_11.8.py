# 8. Калькулятор с операциями

def calculator():
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        operation = input("Enter operation (+, -, *, /): ")

        if operation == "+":
            return a + b

        elif operation == "-":
            return a - b

        elif operation == "*":
            return a * b

        elif operation == "/":
            if b == 0:
                raise ZeroDivisionError("Division by zero is not allowed")
            return a / b

        else:
            raise ValueError(f"Unknown operation: {operation}")

    except ZeroDivisionError as error:
        print("Error:", error)

    except ValueError as error:
        print("Error:", error)

    except Exception:
        print("Error: Invalid input")


result = calculator()
if result is not None:
    print("Result:", result)
