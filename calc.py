#calculator functions for addition subtractionmultiplication and division, factorial, permulation, combination.....

class calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(a,b):
        return(a+b)

    def sub(a,b):
        return(a-b)

    def mult(a, b):
        return(a*b)

    def div(a,b):
        return(a/b)

    def factorial(a):
        fac = 1
        if a >= 0:
          for i in range(1, a+1):
             fac *= i
          return fac
        else:
            return ("MATHS ERROR")
           
    def comb(a,b):
        if a >= b:
            c = calculator.factorial(a-b)

            return (calculator.factorial(a)/c/calculator.factorial(b))
        else:
            return("MATHS ERROR")
    def perm(a,b):
        if a >= b:
            return(calculator.comb(a, b)*calculator.factorial(b))
        else:
            return("MATHS ERROR")

        
class circle:
    def __init__(self, radius):
        self.radius = int(radius)

    def area(self):
        return (self.radius*self.radius*3.1416)
    
    def circum(self):
        return (self.radius*2*3.1416)
