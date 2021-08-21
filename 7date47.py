class Test:
    a=10#static method
    def __init__(self):
        Test.a=20
    @classmethod
    def m1(cls):
        cls.a=30
        Test.a=40
t1=Test()
print(Test.a)
print(t1.a)

"""in this senario our variable is modified but we get output as a 20 20
becoz we are not calling method m1"""
