"""
Whenever control reach the return statment now our function execution,control will
goto outside the function beacuse of that reason always we can define return
statemnet as a last of the function
"""
def f1():
    print("hey")
    x=10
    y=20
    print(x+y)
    print("kunal")
    print("good morning")
f1()
print("bye")
"""
output:
-------
hey
30
kunal
good morning
bye
"""
