"""
The normal argumnet type is depends on the value of that argumnet """
def f1(x):
    print(x,type(x))
f1(3)
f1(3.1)
f1(4j)
f1(True)
f1('kunal')
f1([1,2,3,4])
f1((5,6,76,8))
f1({9,8,7,6})
f1({'name':'kunal','age':21})
"""
output:
=======
3 <class 'int'>
3.1 <class 'float'>
4j <class 'complex'>
True <class 'bool'>
kunal <class 'str'>
[1, 2, 3, 4] <class 'list'>
(5, 6, 76, 8) <class 'tuple'>
{8, 9, 6, 7} <class 'set'>
{'name': 'kunal', 'age': 21} <class 'dict'>
"""
