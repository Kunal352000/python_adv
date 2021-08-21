class Test:
    def m1(cls,self):
        cls.x=10#instance variable bcoz cls act as self
        print("Instance method",cls.x,self)
t1=Test()
t1.m1("Kunal")
