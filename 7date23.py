class student:
    cname="svvv"
    def __init__(self,x,y):
        self.name=x
        self.rollno=y
    def display(self):
        print("Method execution")
        print(self.name)
        print(self.rollno)
s1=student("kunal",101)
s1.display()
s2=student("shivam",102)
s2.display()
s3=student("kj",103)
s3.display()
