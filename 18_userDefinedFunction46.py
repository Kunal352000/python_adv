def f1():
    x=10#local
    print(x)#10
f1()
def f():
    print(x)#error
f()
"""
output:-
10
NameError: name 'x' is not defined
"""
