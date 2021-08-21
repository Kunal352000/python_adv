"""
if we want to modify the non-local variables data with in the inner function,in
that case we are using following syntax:
        nonlocal nonlocalvariablename

once we can modify/update the non-local variables data that is effected remaming
all other cases
"""
def f1():
    x=10
    def f2():
        nonlocal x
        print(x)#10
        x+=5
        print(x)#15
    f2()
    print(x)#15
f1()
"""
output:
10
15
15
"""
