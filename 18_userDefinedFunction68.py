"""
filter():
---------
    filter is a builtin funtion in both python 2.x and python 3.x version

    the filter to return the filter object

    filter(function,iterable obj)

    the filter() takes the one by one element from iterable object to check
    the condition,whenever condition is True the filter() return that element
    otherwise the filter() ignore the element"""
x=[5,3,4,6,7,8,2]
y=filter(lambda i:i%2==0,x)
print(y)
for i in y:
    print(i)
"""
output:
-------
<filter object at 0x00000270ACFC0CD0>
4
6
8
2
"""
