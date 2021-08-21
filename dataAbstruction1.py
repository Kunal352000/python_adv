class test:
    a=10#public variable
    __y=20#private variable
    def m1(self):
        print(test.a)#10
        print(test.__y)#20
t1=test()
t1.m1()
print(t1.a)
print(t1.__y)#error
""" in this secanrio we are getting error becoz we try to access private property
outside of the class
AttributeError: 'test' object has no attribute '__y'
"""
