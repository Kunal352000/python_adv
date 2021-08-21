#create a function to return the no of elements/charcters in a given iterable obj
obj=eval(input("Enter your iterable object: "))
def my_len(x):
    c=0
    for i in x:
        c+=1
    print(c)
my_len(obj)
"""
output:
-------
Enter your iterable object: (1,2,3,4,5,6,7,8,9,0)
10
"""
