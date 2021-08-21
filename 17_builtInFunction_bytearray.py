"""
bytearray()-->bytearray() to return the bytearray object,bytearray object is
a mutable object"""
x=[5,6,7,8]
print(x)
y=bytearray(x)
print(type(y))
"""if we want to print values we use for loop"""
for i in y:
    print(i)
print("*"*25)
print(y[1])#6
y[1]=60
print(y[1])#60 becoz mutable object
print(y)#it always gives byteobject
for j in y:
    print(j)
