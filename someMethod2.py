class Test:
    @staticmethod
    def m1():
        print("someMEthod")
t1=Test()
t1.m1()
Test.m1()
"""in the above example first of all we are declaring decorator and then we are
calling by reference variable and then we are calling by classname thats why this
progarm is executed"""
