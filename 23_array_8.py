#mutable array elements
import array
a=array.array('i',[1,2,3,4,5])
print(a)
a[1]=30
print(a)
a.append(6)
print(a)
a.append(7)
print(a)
a.pop(6)
print(a)
a.pop()
print(a)
a.remove(30)
print(a)
"""
output:
-------
array('i', [1, 2, 3, 4, 5])
array('i', [1, 30, 3, 4, 5])
array('i', [1, 30, 3, 4, 5, 6])
array('i', [1, 30, 3, 4, 5, 6, 7])
array('i', [1, 30, 3, 4, 5, 6])
array('i', [1, 30, 3, 4, 5])
array('i', [1, 3, 4, 5])
"""
