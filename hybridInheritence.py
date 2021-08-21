class x:
    def m1(self):
        print("i am in m1")
class y(x):
    def m2(self):
        print("i am in m2")
class a(y):
    def m3(self):
        print("i am in m3")
class b(y):
    def m4(self):
        print("i am in m4")
class c(a,b):
    def m5(self):
        print("i am in m5")
c1=c()
c1.m1()
c1.m2()
c1.m3()
c1.m4()
c1.m5()
print(c.mro())
