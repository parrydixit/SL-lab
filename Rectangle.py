class rectangle:

    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        print("Area of rectangle is: ", (self.length * self.breadth))


a = int(input("Length:"))
b = int(input("Breadth:"))

r1 = rectangle(a, b)
r1.area()
