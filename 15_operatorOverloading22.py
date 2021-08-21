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
print('This month salary:',e*t)

"""Output--->This month salary: 2000

   whenever control reach at print statemnet and see e*t it check for e refernce
   there is object or not and then * it calls magic meythod now t checked and
   perform multiplication and gives output"""
