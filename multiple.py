class x:
    def m1(self):
        print("I am in m1")
class y:
    def m2(self):
        print("I am in m2")
class z(x,y):
    def m3(self):
        print("I am in m3")
z1=z()
z1.m1()
z1.m2()
z1.m3()
print(z.mro())#list format
print(z.__mro__)#tuple format
#multiple inheritence
