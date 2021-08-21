class test:
    x=10
    __y=20
    def m1(self):
        print(test.x)#10
        print(test.__y)#20
t1=test()
t1.m1()
print(t1.x)#10
print(t1._test__y)#20
