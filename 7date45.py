class Test:
    a=10#static method
    def __init__(self):
        print("Inside constructor")
        print(self.a)
        print(Test.a)
    def m1(self):
        print("inside method")
        print(self.a)
        print(Test.a)
    @classmethod
    def m2(cls):
        print("Inside classmethd")
        print(Test.a)
        print(cls.a)
    @staticmethod
    def m3():
        print("Inside static method")
        print(Test.a)
t1=Test()
t1.m1()
t1.m2()
t1.m3()
print("Outside of a class.")
print(Test.a)
print(t1.a)

