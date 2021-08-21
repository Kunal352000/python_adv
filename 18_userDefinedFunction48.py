"""
global variable:
    we can define a variable above the function definition or at the begning
    of the program that type of variable are called global vbariable

    we can access the global variable data any where in our program
"""
x=10#global
def f1():
    print(x)#10
f1()
print(x)#10
def f2():
    print(x)#10
f2()
"""
output:
10
10
10
"""
