"""
kw args:-
=========
    kw args takes 0 or more keyword argumnets
    by default kw args type is dict

    syntax:
    -------
            def functionname(**parameter):
                    ------------
                    ------------
"""
def f1(**kwargs):
    print(kwargs,type(kwargs))
f1()
"""
output:{} <class 'dict'>

if we are passing 0 value then we recive empty dict and **kwargs type is dict"""
