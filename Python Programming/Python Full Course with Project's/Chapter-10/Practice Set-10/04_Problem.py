class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"This square is {self.n * self.n}")

    def cube(self):
        print(f"This cube is {self.n * self.n * self.n}")

    def squareroot(self):
        print(f"This squareroot is {self.n**1 / 2}")

    @staticmethod
    def greet():
        print("Hello Their!")


a = Calculator(4)
a.square()
a.cube()
a.squareroot()
