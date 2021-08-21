class Employee:
    '''This class is developed by kunal sir'''
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
e1=Employee(100,"kunaldada",100000000,"Newyork")
e1.info()
e2=Employee(101,"shivamdada",200000000,"america")
e2.info
