"""
anonymus function:
------------------
    we can define/create a function without using a function name that type of
    function are called anonymus function

    we can define/create a normal function by using "def" keyword

    we can define/create anonymus function by using lambda keyword,beacuse of
    that reason anonymus functions are called lambda function

    Syntax:--> lambda arguments:expression
    """
def add(x,y):
    z=x+y
    return z
print(add(3,4))
print(type(add))

#or
add1=lambda x,y : x+y
print(add1(5,5))
print(type(add1))
"""
output:-
7
<class 'function'>
10
<class 'function'>
"""
