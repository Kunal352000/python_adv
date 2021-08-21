class Test:
    a=10#static variable
    def __init__(self):
        print("Inside constructor.")
        print(self.a)#accesing static variable inside class by using self
        print(Test.a)#accesing static variable inside class by using Classname
    def m1(self):
        print("Inside method")
        print(Test.a)#accesing static variable inside class by using Classname
        print(self.a)#accesing static variable inside class by using self
t1=Test()
t1.m1()
