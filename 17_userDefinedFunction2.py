"""
2)default arguments/paramters:
==============================
    the programmer/developer to assign the values to the parameters at the time
    of function defination,that type of parameters are called default parameters/
    arguments"""
def add(x=1,y=2):
    z=x+y
    print(z)
add()
add(5,5)
add(6)
add(0,8)
"""
ouput:
------
3
10
8
8
"""
