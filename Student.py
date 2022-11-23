class Student:

    def __init__(self):
        self.name= input("Enter the name of the student:")
        self.age= int(input("Enter the age of student:"))
        self.marks=[]

    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print(self.marks)

    def accept(self):
        phy= int(input("Physics: "))
        che= int(input("Chemistry: "))
        maths= int(input("Maths: "))
        self.marks.append(phy)
        self.marks.append(che)
        self.marks.append(maths)


s1= Student()
s1.accept()
s1.display()