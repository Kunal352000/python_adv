l=[1,2,3,4,5,6,7,8,9,10]
s=list(filter(lambda x:x%2==0,l))
print(s)
s1=list(filter(lambda x:x%2!=0,l))
print(s1)
"""
output:
-------
[2, 4, 6, 8, 10]
"""

