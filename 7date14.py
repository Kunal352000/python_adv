class student:
    '''The class is developed by kunaldada'''
    def __init__(self,rollno,name):
        self.rollno=rollno
        self.name=name
    def talk(self):
        print("Hello my name is:",self.rollno)
        print("my roll no is:",self.name)
s1=student(101,"kunalbaba")
s1.talk()
s2=student(102,"shivamdada")
s2.talk()
