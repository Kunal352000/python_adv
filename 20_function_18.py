"""
in python call by value/pass by value our original data is not modified
"""
x=[1,2,3]
def f1(y):
    print(y)
    y=[10,20,30]
    print(y)
f1(x)
print(x)
"""
output:
--------
[1, 2, 3]
[10, 20, 30]
[1, 2, 3]
"""
