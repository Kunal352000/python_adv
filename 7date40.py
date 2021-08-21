class Test:
    a=10
    def __init__(self):
        Test.b=20#static
    def m1(self):
        Test.c=30#static
t1=Test()
print(Test.a,Test.b,Test.c)
