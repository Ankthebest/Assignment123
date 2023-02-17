class Calculator:

    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
        
    def add(self):
        add = self.num1+self.num2
        return add

    def subtract(self):
        subtract = self.num2-self.num1
        return subtract 

    def multiply(self):
        mul = self.num1*self.num2
        return mul 

    def divide(self):
        div = self.num2/self.num1
        return div 


obj = Calculator(10, 94)
print(obj.add())
print(obj.subtract())
print(obj.multiply())
print(obj.divide())