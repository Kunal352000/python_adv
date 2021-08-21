def f1(*x,y,**z):
    print(x,type(x))
    print(y,type(y))
    print(z,type(z))
f1(3.2,4j,False,name="kunal",age=21)
"""
output:
-------
TypeError: f1() missing 1 required keyword-only argument: 'y'

this program gives error becoz we are not mentioing y in function calling if we follow
this syntax y="222" then program run suceesfully"""
