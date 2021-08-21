class student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def __lt__(self,other):
        return self.marks<other.marks
s1=student('shivam',101)
s2=student("kkk",102)
print(s1<s2)#True
print(s2<s1)#false
