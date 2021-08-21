class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
s1=Student()
s1.setname("kunal")
s1.setmarks(199)

print("Student name:",s1.getname())
print("Student marks:",s1.getmarks())
