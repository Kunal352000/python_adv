"""
in python,directly we cant modify the global variable data with in the function
"""
x=100#gloabl
def f1():
    print(x)
    x+=5
    print(x)
f1()
print(x)
def f2():
    print(x)
f2()
"""
output:-UnboundLocalError: local variable 'x' referenced before assignment
"""
