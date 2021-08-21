"""
map():-
-----
    map() is a builtin function in python2.x and python 3.x
    map() to return the map object
    map(function,*iterableobj)
    the map(),takes the one by one element from the given iterable objects
    to perform the operation and to return the result"""
x=[5,3,4,6,7,8,2]
y=map(lambda i:i%2==0,x)
print(y)
for ele in y:
    print(ele)
"""
output:
-------
<map object at 0x00000220F4C40CD0>
False
False
True
True
False
True
True
"""
