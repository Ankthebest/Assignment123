class Point:

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        sqSum = self.x**2+self.y**2+self.z**2
        print("Sum of sqaures :",sqSum)

obj = Point(6,4,3)    
obj.sqSum()
