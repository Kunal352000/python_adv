class test:
    def m1(self,a,b):
        print("good morning")
    def m1(self):
        print("hai")
    def m1(self,a):
        print("Hello")
t1=test()
#t1.m1()#error
#t1.m1(4,5)#error
t1.m1('a')
