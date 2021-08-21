class Student:
    """The class is developed by kj"""
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name
    def talk(self):
        print("Hello my name is",self.name)
        print("My roll nuber is",self.rollno)
s=Student(101,"kunal")
print(s.name)
print(s.rollno)
s.talk()

s1=Student(102,"shivam")
s1.talk()

s3=Student(103,"kj")
s3.talk()
