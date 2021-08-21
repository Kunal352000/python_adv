class test:
    """constructor overloading by variable length argument"""
    def m1(self):
        print("no-arg method")
    def m1(self,a):
        print("one-arg method")
    def m1(self,a,b):
        print("tow-arg method")
t=test()
t.m1(10)
