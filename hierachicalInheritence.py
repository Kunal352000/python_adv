class x:
    def m1(self):
        print("i am in m1")
class y(x):
    def m2(self):
        print("i am in m2")
class z(x):
    def m3(self):
        print("i am in m3")
z1=z()
z1.m3()
z1.m1()
print("*"*20)
y1=y()
y1.m2()
y1.m1()
