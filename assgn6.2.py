class Dog:
    def __init__(self,name,age,coat_color):
        self.name=name
        self.age=age
        self.coat_color=coat_color

    def description(self):
        print("Name of dog :",self.name,"Age :",self.age)

    def get_info(self):
        print("Coat color of dog :",self.coat_color)


class JackRussellTerrier(Dog):

    def birthmark(self,birthmark):
        
        return None if birthmark == None else 1

    def foods(self):
        print("Dog has food 3 times a day!")

       
class Bulldog(Dog):
    def weight(self,weight):
        if weight > 24:
            print("The dog is grown heavy!")
        else:
            print("The dog is light weight!")

    def food(self,breads):
        breads = int(input("Enter no. of breads dog has at a time :"))
        times = input("Enter 2 for {twice} or 3 for {thrice} :")
        print(f"The dog eats {breads} breads {times} a day")

demo1=JackRussellTerrier('Jimmy',7,'brown')
demo1.description()
demo1.get_info()
print(demo1.birthmark(0))
demo1.foods()

demo2=Bulldog('Yono',5,'Black')
demo2.description()
demo2.get_info()
demo2.weight(24)
demo2.food(4)