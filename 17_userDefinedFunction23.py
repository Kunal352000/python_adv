def f1(x,*y,**z):
    print(x,type(x))
    print(y,type(y))
    print(z,type(z))
f1()
"""
output:TypeError: f1() missing 1 required positional argument: 'x'

in this above example we get error becoz its mandtory to pass value to the
normal argumnet
"""
