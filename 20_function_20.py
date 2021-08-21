"""
function overloading:
---------------------
    The concept of defining multiple functions with same name and differnet no.of
    parameters with in the same program is known as function overloading"""
def f1():
    print("hey")
def f1(a):
    print("kunal")
def f1(a,b):
    print("good morning")
#f1()
#f1(4)
f1(4,5)
"""
output:
-------
good morning
"""
