x=100#global
class Test:
    x=777#static variable
    def m1(self):
        x=888
        print(x)#888
t1=Test()
t1.m1()

"""Output is 888 becoz we are calling method in method local variable"""
        
