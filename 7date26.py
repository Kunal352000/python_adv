class student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def info(self):
        self.marks=90
s1=student("kunal",101)
s1.info()
print(s1.__dict__)
