#calculator functions for addition subtractionmultiplication and division, factorial....

class calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(a,b):
        print(a+b)

    def sub(a,b):
        print(a-b)

    def mult(a, b):
        print(a*b)

    def div(a,b):
        print(a/b)

    def factorial(a):
        fac = 1
        for i in range (1, a+1):
            fac *= i
        print(fac)


