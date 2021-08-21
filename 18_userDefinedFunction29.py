def f1(x,*y,**z):
    print(x,type(x))
    print(y,type(y))
    print(z,type(z))
f1(3.2,4j,False,9,name="kunal",age=21)
#   x     *y             **z
"""
output:
-------
3.2 <class 'float'>
(4j, False, 9) <class 'tuple'>
{'name': 'kunal', 'age': 21} <class 'dict'>
"""
