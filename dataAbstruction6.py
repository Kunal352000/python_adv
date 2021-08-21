class test:
    x=10#public
    _y=20#protected
    __z=30#private
    def m1(self):
        print(test.x)
        print(test._y)
        print(test.__z)
t1=test()
t1.m1()
print(t1.x)
print(t1._y)
print(t1._test__z)
