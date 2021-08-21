class Test:
    a=10#static method
    def __init__(self):
        Test.a=20#modify static varibale
    @classmethod
    def m1(cls):
        cls.a=30#modify static variable
        Test.a=40#modify static variable
t1=Test()
t1.m1()
print(Test.a)
print(t1.a)


