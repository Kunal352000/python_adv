class sample:
    def m1(self):
        print("good morning")
class test:
    def m1(self):
        print("hai")
class demo(sample,test):
    def m1(self):
        super().m1()
        print("hello")
d1=demo()
d1.m1()
