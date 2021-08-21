class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def info(self):
        print("HEllo my name is",self.name)
        print("my roll number is",self.rollno)
s1=student("kunal",101)
s1.info()
print(s1.name,s1.rollno)
s2=student("shivam",102)
s2.info()
