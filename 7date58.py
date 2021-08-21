x=100#global
class Test:
    def m1(self):
        x=888#local variable
        print(x)
    def m2(self):
        print(x)#in this global variable
t=Test()
t.m1()
t.m2()
        
