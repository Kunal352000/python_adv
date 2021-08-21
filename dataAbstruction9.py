class test:
    def m1(self):
        print("i am in public instance method-m1")
    def _m2(self):
        print("i am in protected method-m2")
        self.m1()
    def __m3(self):
        print("i am in private method-m3")
        self._m2()
        self.m1()
t1=test()
t1.m1()
t1._m2()
t1._test__m3()
