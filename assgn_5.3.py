class Student:

    def setName(self,__name):
        self.__name = __name
    def getName(self):
        return self.__name
    def setRollNumber(self,__roll_no):
        self.__roll_no = __roll_no
    def getRollNumber(self):
        return self.__roll_no

obj = Student()
obj.setName("Rahul")
obj.setRollNumber(25)
print(obj.getName())
print(obj.getRollNumber())