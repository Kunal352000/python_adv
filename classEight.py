class Employee:
    def __init__(self,eno,ename,esal,eaddr):
        self.eno=eno
        self.ename=ename
        self.esal=esal
        self.eaddr=eaddr
    def info(self):
        print("Employee number:",self.eno)
        print("Employee name:",self.ename)
        print("Employee salary:",self.esal)
        print("Employee address:",self.eaddr)
e1=Employee(100,'kunal',1000,'hyd')
e1.info()
e2=Employee(200,'shivam',2000,'indore')
e2.info()
