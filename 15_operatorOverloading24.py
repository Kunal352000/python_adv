class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __mul__(self,other):#interpreter ignores this method
        return self.salary*other.days
class Timesheet:
    def __init__(self,name,days):
        self.name=name
        self.days=days
    def __mul__(self,other):
        return self.days*other.salary
e=Employee('kunal',100)
t=Timesheet('shivam',20)
print('This month salary:',t*e)

