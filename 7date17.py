class Employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr
    def info(self):
        print(self.eno)
        print(self.ename)
        print(self.esal)
        print(self.eaddr)
e1=Employee(100,"kunal",100000000,"newyork")
e1.info()
print("*"*40)
e2=Employee(200,"kunallover",100000,"newyork")
e2.info()
