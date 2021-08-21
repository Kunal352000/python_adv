class test:
    def m1(self):
        self.x=10#public instance variable
        self._y=20#protected instance variable
        self.__z=30#private instance variable
        print(self.x)#10
        print(self._y)#20
        print(self._test__z)#30
t1=test()
t1.m1()
print(t1.x)#10
print(t1._y)#20
print(t1._test__z)#30
