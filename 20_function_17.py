"""
call by value/pass by reference:
--------------------------------
    in call by value/pass by value,our original value is not modified
    """
x=10
def f1(y):
    print(y)
    y+=5
    print(y)
f1(x)
print(x)
#f1(x)
#print(x)
"""
output:
-------
10
15
10
"""
