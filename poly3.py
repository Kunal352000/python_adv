class test:
    def m1(self):
        print("hello")
class demo(test):
    def m1(self):
        print("hey")
d1=demo()
d1.m1()
"""we recive output as hey becoz we are creating demo class object
and we are calling a method by demo reference object"""
