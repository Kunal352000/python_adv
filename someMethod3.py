class Test:
    def m1(x):
        print("some method",x)
t=Test()
t.m1(10)
"""
TypeError: m1() takes 1 positional argument but 2 were given
This is invalid becoz first argument is not self,suppose if it is self then we
are not defining other argument and we are calling method in that time we
are passing 10 as a parameter but in method declartion there is only one
argument x thats why we get error
"""
