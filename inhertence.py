class Test:
    x=10
    def m1(self):
        self.y=20
        print(Test.x)
        print(self.y)
class Demo(Test):
    a=1
    def m2(self):
        self.b=2
        print(Demo.a)
        print(self.b)
        print(Demo.x)
        print(self.y)
d1=Demo()
d1.m1()
d1.m2()
