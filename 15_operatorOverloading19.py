class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
s1=student('kunal',100)
s2=student("shivam",201)
print(s1<s2)

"""output:-TypeError: '<' not supported between instances of 'student' and 'student'

we get error becoz we are not using magic method in class"""
