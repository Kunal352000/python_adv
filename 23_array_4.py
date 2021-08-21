"""to get the individual element address in our array"""
import array
x=array.array('i',[2,3,4])
print(x)
print(type(x))
print(x.byteswap())
print(x)
"""
output:
-------
array('i', [2, 3, 4])
<class 'array.array'>
None
array('i', [33554432, 50331648, 67108864])
"""
