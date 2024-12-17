# 2. Write a class “Calculator” capable of finding square, cube and square root of a number. 

class Calculator:
    def __init__(self, number):
        self.number = number
        
    def square(self):
            return self.number ** 2
    
    def cube(self):
        return self.number ** 3
    
    def square_root(self):
        if self.number < 0:
            return "Error: Square root of negative number is not a real number."
        else:
            return self.number ** 0.5
        
number = float(input('Enter any number here: '))
calc = Calculator(number)
print(f"The square of {number} is {calc.square()}")
print(f"The cube of {number} is {calc.cube()}")
print(f"The square root of {number} is {calc.square_root()}")

    