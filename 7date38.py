class Student:
    cname="svvv"
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
s1=Student("kunal",101)
s2=Student("shivam",102)
print(s1.name,s1.rollno,Student.cname)
print(s2.name,s2.rollno,Student.cname)



