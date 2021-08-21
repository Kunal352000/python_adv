class Test:
    def m1(self):
        self.x=10
        y=20
        print(self.x)
        print(y)
    def m2(self):
        print(self.x)
        print(y)
t1=Test()
t1.m1()
t1.m2()
