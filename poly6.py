class sample:
    def m1(self):
        print("good morning")
class test(sample):
    def m1(self):
        super().m1()
        print("hey")
class demo(test):
    def m1(self):
        super().m1()
        print("hello")
d1=demo()
d1.m1()

