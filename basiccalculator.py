# basic calculator

class Calculator():
    def plus(self):
        value1 = int(input("provide value 1: "))
        value2 = int(input("provide value 2: "))
        result = value1 + value2
        print(f"{value1} + {value2} = {result}")
    def minus(self):
        value1 = int(input("provide value 1: "))
        value2 = int(input("provide value 2: "))
        result = value1 - value2
        print(f"{value1} - {value2} = {result}")
    def multiply(self):
        value1 = int(input("provide value 1: "))
        value2 = int(input("provide value 2: "))
        result = value1 * value2
        print(f"{value1} * {value2} = {result}")
    def divide(self):
        value1 = int(input("provide value 1: "))
        value2 = int(input("provide value 2: "))
        result = value1 / value2
        print(f"{value1} / {value2} = {result}")
        
my_cal = Calculator()
my_cal.plus()
my_cal.minus()
my_cal.multiply()
my_cal.divide()
    