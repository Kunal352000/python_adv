import random
x=[12,2.1,4j,"kunal",True,(8,8)]
random.shuffle(x)
print(x)
random.shuffle(x)
print(x)
random.shuffle(x)
print(x)
"""
output:
--------
[12, 4j, 'kunal', 2.1, (8, 8), True]
[True, 'kunal', 12, (8, 8), 4j, 2.1]
[True, 4j, 'kunal', (8, 8), 2.1, 12]
"""
