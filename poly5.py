class test:
    def m1(self):
        print("hey")
class demo(test):
    def m1(self):
        print("hello")
        super().m1()
d1=demo()
d1.m1()
"""we recive output as hello and hey becoz in class demo we are writing
super()method. after print statment"""

