class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def display(self):
        print("Hey",self.name)
        print("Your marks is:",self.marks)
    def grade(self):
        if self.marks>60:
            print("First grade:")
        elif self.marks>=50:
            print("Second garde:")
        elif self.marks>=35:
            print("You got third grade:")
        else:
            print("You are failed")
n=int(input("Enter number of student: "))
for i in range(n):
    name=input("Enter Student name name: ")
    marks=float(input("Enter student marks marks:"))
    s1=Student(name,marks)
    s1.display()
    s1.grade()
    print("*"*20)
    
