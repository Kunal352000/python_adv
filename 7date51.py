class Test:
    a=10
    def m1(self):
        self.a=20
t1=Test()
t1.m1()
print(Test.a)#10
print(t1.a)#20
