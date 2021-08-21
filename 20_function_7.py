"""
reduce():
---------
    the reduce() is builtin function in python2.x but reduce() is not a builtin
    function in python 3.x
    the reduce(),to reduce the no.of elements into single element
    reduce() function reduces sequence of elements into a single element by applying
    the specified function.
    """
from functools import*
l1=[10,20,30,40]
print(reduce(lambda x,y:x+y,l1))
    
