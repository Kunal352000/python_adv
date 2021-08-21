"""
non-local variable:-
--------------------
    we can define the variables with in the outer function and above the inner
    function,that type of variable are called non-local vbariables to inner
    functiom

    we can acess the non-local variables data with in outer function(inside
    the inner function and outside the inner function) only.
    """
def f1():
    x=10
    def f2():
        print(x)#10
    f2()
    print(x)#10
f1()
print(x)#error
"""
output:
10
10
Traceback (most recent call last):
  File "C:/Users/Dell/Desktop/18_userDefinedFunction51.py", line 18, in <module>
    print(x)#error
NameError: name 'x' is not defined
"""
