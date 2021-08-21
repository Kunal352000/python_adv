class Employee:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
    def __mul__(self,other):
        return self.salary*other.days
class Timesheet:
    def __init__(self,name,days):
        self.name=name
        self.days=days
    
e=Employee('kunal',100)
t=Timesheet('shivam',20)
print('This month salary:',t*e)

"""output-->TypeError: unsupported operand type(s) for *: 'Timesheet' and 'Employee'

in this program we get error becoz whenever contraol reach at t in checks in timeshhet
class there is magic method or not if not then give us error"""
