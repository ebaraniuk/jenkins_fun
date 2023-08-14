class Foo:

    def __init__(self, x: int):
        self.x = x

    def __add__(self, other):
        return self.x + other

    def factorial(self):
        fact = 1
        for i in range(1, self.x + 1):
            fact *= i
        return fact
