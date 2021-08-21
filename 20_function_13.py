"""create a function to return maximum element from the given iterable object"""
obj=eval(input("Enter iterable object"))
def my_max(x):
    m=x[0]
    for i in x:
        if m<i:
            m=i
    print(m)
my_max(obj)
"""
output:
-------
Enter iterable object"shivamjoshi"
v

Enter iterable object(12,13,14,12,15,17)
17
"""
