"""
whenever control reach the return statment now our function execution,control
will goto outside of the function beacuse of that reason always we can define
return statment as a last statment"""
def f1():
    print("hey")
    x=10
    y=20
    return x+y
    print("kunal")
    print("good morning")
print(f1())
print("bye bye")
"""
output:
-------
hey
30
bye bye


in python we can return multiple values also possible,by default these values
will be wriiten as a tuple format."""
