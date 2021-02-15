class Calculator():
    def __init__(self) -> None:
        self.memory = 0

    def add(self, num1: float, num2: float = None) -> float:
        """Adds two given numbers.
        If given only one number, adds to memory (0 or last result)."""
        if num2 is None:
            result = self.memory + num1
            self.memory = result
        else:
            result = num1 + num2
            self.memory = result
        return result

    def subtract(self, num1: float, num2: float = None) -> float:
        """Subtracts two given numbers (second from first).
        If given only one number, subtracts from memory (0 or last result)."""
        if num2 is None:
            result = self.memory - num1
            self.memory = result
        else:
            result = num1 - num2
            self.memory = result
        return result

    def multiply(self, num1: float, num2: float = None) -> float:
        """Multiply two given numbers.
        If given only one number, multiply by memory (0 or last result)."""
        if num2 is None:
            result = self.memory * num1
            self.memory = result
        else:
            result = num1 * num2
            self.memory = result
        return result

    def divide(self, num1: float, num2: float = None) -> float:
        """Divide two given numbers, first number by second number.
        If given only one number, divides memory (0 or last result) by it."""
        if num2 is None:
            result = self.memory / num1
            self.memory = result
        else:
            result = num1 / num2
            self.memory = result
        return result

    def take_root(self, num1: float, num2: float = None) -> float:
        """Takes n root of number, where:
            * n - second given number,
            * number - first given number.
        If given only one number, takes memory (0 or last result) root of it."""
        if num2 == 0:
            self.memory = 0
            return 0
        if num2 is None and self.memory == 0:
            return 0
        if num2 is None and self.memory != 0:
            result = num1 ** (1 / self.memory)
            self.memory = result
        else:
            result = num1 ** (1 / num2)
            self.memory = result
        return result

    def reset_memory(self):
        """Resets memory to zero."""
        return self.memory == 0
