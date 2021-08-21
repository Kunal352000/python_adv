class student:
    def setName(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setMarks(self,marks):
        self.marks=marks
    def getMarks(self):
        return self.marks
n=int(input("Enter number your of student: "))
for i in range(n):
    name=input("Enter student name: ")
    marks=int(input("Enter {} marks: ".format(name)))
    s=student()
    s.setName(name)
    s.setMarks(marks)
    print('*'*29)
    print("Student name:",s.getName())
    print("Marks are:",s.getMarks())
    print('*'*29)
        
