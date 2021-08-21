class Test:
    x=[1,2,3]
    def m1(self):
        self.y=[10,20,30]
        print(id(Test.x))
        print(id(self.y))
t1=Test()
t1.m1()
t1.m1()
t1.m1()
t2=Test()
t2.m1()
t2.m1()
