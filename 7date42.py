class Test:
    a=10#static variable
    def __init__(self):
        Test.b=20#static variable
    def m1(self):
        Test.c=30#static variable
    @classmethod
    def m2(cls):
        cls.d=40#static variable
        Test.e=50#static variable
    @staticmethod
    def m3():
        Test.f=60#static variable
T1=Test()
Test.g=70#static variable
T1.m1()
Test.m2()
Test.m3()
print(Test.__dict__)

"""we can call a classmethod and static method by using classname"""
