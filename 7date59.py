class Test:
    def m1(self):
        x=888#local variable
        print(x)
    def m2(self):
        print(x)#error bcoz we are accesing local variable outside of class
t=Test()
t.m1()
t.m2()
        
