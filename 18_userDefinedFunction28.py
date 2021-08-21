def f1(x,*y,**z):
    print(x,type(x))
    print(y,type(y))
    print(z,type(z))
f1(2)#this executes
f1()#this give error
"""
output:
-------
2 <class 'int'>
() <class 'tuple'>
{} <class 'dict'>

TypeError: f1() missing 1 required positional argument: 'x'

"""
