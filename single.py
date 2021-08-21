class x:
    def m1(self):
        print("i am in m1")
class y(x):
    def m2(self):
        print("i am in m2")
y1=y()
y1.m1()#calling m1 by using y object reference becoz we inherit x
y1.m2()
        
