"""
kw args:-
=========
    kw args takes 0 or more keyword arguments
    by default kw args type is dict
    syntax:-
    ========
        def functionname(**parameter):
            --------
            --------
            --------
"""
def f1(**x):
    print(x,type(x))
f1()

"""
output:{} <class 'dict'>

whenever we are not passing any value then also our program succesfully executed
but it gives empty dict
"""
