"""
bytes()-->bytes to return the bytes object,bytes object is immutabble object
"""
x=[4,5,6,7]
print(x)
y=bytes(x)
print(y)
print(id(y))
""" if we want to print one by one value we use for loop"""
for i in y:
    print(i)
print(y[1])#5
y[1]=50
print(y[1])#error becoz bytes dont support modification


