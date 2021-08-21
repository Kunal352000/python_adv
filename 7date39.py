class Student:
    cname="svvv"
    def __init__(self,name,rollno):
        Student.add="indore"
        self.name=name
        self.rollno=rollno
s1=Student("kunal",101)
print(s1.name,s1.rollno,Student.cname,Student.add)

"""In this we are decalering a static variable inside constructor by using
class name and access the static variable outside with class name"""



