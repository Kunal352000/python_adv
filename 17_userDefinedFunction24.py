def f1(x,*y,**z):
    print(x,type(x))
    print(y,type(y))
    print(z,type(z))
f1(199)
"""
output:
        199 <class 'int'>
        () <class 'tuple'>
        {} <class 'dict'>

it is mandatary to pass value to the normal argument,but its not mandotory to
pass value to the args and kwargs"""
