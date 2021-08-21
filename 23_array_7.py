#slicing and indexing
import array
a=array.array('i',[1,2,3,4,5,6,7])
print(a)
print(a[1])
print(a[-2])
print(a[2:])
print(a[:3])
print(a[::])
print(a[::-1])
"""
output:
--------
array('i', [1, 2, 3, 4, 5, 6, 7])
2
6
array('i', [3, 4, 5, 6, 7])
array('i', [1, 2, 3])
array('i', [1, 2, 3, 4, 5, 6, 7])
array('i', [7, 6, 5, 4, 3, 2, 1])
"""
