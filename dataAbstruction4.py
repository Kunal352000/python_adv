class test:
    x=10
    __y=20
    def m1(self):
        print(test.x)#10
        print(test.__y)#20
class demo(test):
    def m2(self):
        print(demo.x)#10
        print(demo._test__y)#20
d1=demo()
d1.m1()
d1.m2()
