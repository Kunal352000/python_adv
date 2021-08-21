"""
if we want to update/modifiy the global variable data with in th function in that
case we are using folowing syntax.
    global variablename

once we modify the global variables data,that is effected in remaining all other
cases
"""
x=10#global
def f1():
    global x
    print(x)#10
    x+=5
    print(x)#15
f1()
print(x)#15
def f2():
    print(x)#15
f2()
print(x)#15
"""
output:
10
15
15
15
15
"""
