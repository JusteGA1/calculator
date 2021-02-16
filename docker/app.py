from calculator.calculator import Calculator

calculator = Calculator()

result = calculator.add(5, 7)
print(f"5 + 7 = {result}")

result = calculator.subtract(3)
print(f"in_memory_value - 3 = {result}")

calculator.reset_memory()
