class Person:
    def __init__(self,age):
        self.intialAge=age
        if self.intialAge<0:
            self.age=0
            print("Age is not valid,setting age to 0.")
        else:
            self.age=self.intialAge
        
    def yearPasses(self):
        self.age=self.age+1
        
    def amIOld(self):
        if self.age<13:
            print("You are young.")
        elif self.age>12 and self.age<18:
            print("You are teenger.")
        else:
            print("You are old.")
        
    
        

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")
