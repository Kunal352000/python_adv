def isEven(x):
    if x%2==0:
        return True
    else:
        return False
l=[1,2,3,4,5,6,7,8]
print(list(filter(isEven,l)))
"""
Output:
-------
[2, 4, 6, 8]
"""
