"""
in python,direcly we cant modify the non-local variables data with in the inner
function"""
def f1():
    x=10
    def f2():
        print(x)
        x+=5
        print(x)
    f2()
    print(x)
f1()
"""
output:UnboundLocalError: local variable 'x' referenced before assignment
"""
