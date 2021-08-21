class student:
    def __init__(self,name,rollno):
        print("Constructor execution..")
        self.name=name
        self.rollno=rollno
    def display(self):
        print("method execution")
        print("Hello my name is:",self.name)
        print("my roll number is:",self.rollno)
s=student("kunalji",101)
s.display()
