class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def info(self):
        self.marks=50
s1=student("kunal",101)
s1.info()
print(s1.__dict__)
s1.age=21
print(s1.__dict__)

s2=student("shivam",102)
s2.age=22
print(s2.__dict__)
