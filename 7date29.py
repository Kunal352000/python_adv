class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def display(self):
        print("HEllo my name is",self.name)
        print("my rollNo is",self.rollno)
s1=student("kunal",101)
s1.display()
