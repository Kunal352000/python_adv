class Test:
    a=10#static method
    def __init__(self):
        Test.a=20#modify static varibale
    @classmethod
    def m1(cls):
        cls.a=30#modify static variable
        Test.a=40#modify static variable
    @staticmethod
    def m2():
        Test.a=50
t1=Test()
t1.m1()
t1.m2()
Test.a=60#modify static variable outside of class by using classname
print(Test.a)
print(t1.a)


