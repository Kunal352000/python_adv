x=100#global variable
class Test:
    x=888#static variable
    def m1(self):
        print(x)#100
        print(self.x)#888
    def m2(self):
        print(x)
        print(Test.x)
t1=Test()
t1.m1()
t1.m2()
