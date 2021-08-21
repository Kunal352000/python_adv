def f1(*x,y,**z):
    print(x,type(x))
    print(y,type(y))
    print(z,type(z))
f1(3.2,4j,False,name="kunal",age="21",y="222")
"""
output:-
(3.2, 4j, False) <class 'tuple'>
222 <class 'str'>
{'name': 'kunal', 'age': '21'} <class 'dict'>
"""
