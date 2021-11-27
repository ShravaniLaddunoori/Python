class rectangle():
    def __init__(self,breadth,length):
        self.breadth = breadth
        self.length = length
    def area(self):
        return self.breadth * self.length
b = int(input('Enter breadth of rectangle:'))
l = int(input('Enter length of rectangle:'))
obj = rectangle(b,l)
print('Area of rectangle:',obj.area())
