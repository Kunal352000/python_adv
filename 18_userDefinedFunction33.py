def f1(*x,y,**z):
    print(x,type(x))
    print(y,type(y))
    print(z,type(z))
f1(3.2,4j,False,y=9,name="kunal",age=21)
"""
output:
(3.2, 4j, False) <class 'tuple'>
9 <class 'int'>
{'name': 'kunal', 'age': 21} <class 'dict'>
"""
