class test:
    def m1(self):
        print("hey")
class demo(test):
    def m1(self):
        super().m1()
        print("hello")
d1=demo()
d1.m1()
"""we recive output as hey and hello becoz in class demo we are writing
super()method."""

