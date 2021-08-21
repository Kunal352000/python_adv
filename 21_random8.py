import random
x=[12,2.1,True,4j,'kunal',(10,10)]
print(random.choices(x))
print(random.choices(x))
print(random.choices(x))
print(random.choices(x))
print(random.choices(x,k=2))
print(random.choices(x,k=2))
print(random.choices(x,k=2))
print(random.choices(x,k=3))
print(random.choices(x,k=3))
print(random.choices(x,k=3))
"""
output:
-------
[4j]
['kunal']
[12]
[4j]
[True, 'kunal']
[True, (10, 10)]
[True, True]
[True, (10, 10), 'kunal']
[4j, 12, 'kunal']
[True, True, True]
"""

