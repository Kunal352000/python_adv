class Test:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30
    def m1(self):
        self.d=40
    def m2(self):
        self.e=50
t1=Test()
t1.m1()
print(t1.__dict__)
t2=Test()
t2.m1()
t2.f=60
t2.g=70
print(t2.__dict__)
