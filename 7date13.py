class test:
    x=[1,2,3]
    def __init__(self):
        self.y=[10,20,30]
    def m1(self):
        print(id(test.x))
        print(id(self.y))
t1=test()
t1.m1()
t1.m1()
t1.m1()
t2=test()
t2.m1()
t2.m1()
