"""create a function to return the elements in reverse order from the given
iterable object"""
obj=eval(input("Enter iterable object: "))
def my_rev(x):
    y=[]
    for i in range(len(x)-1,-1,-1):
        y.append(x[i])
    print(y)
my_rev(obj)
"""
output:
-------
Enter iterable object: [10,20,30,40,50,60,70]
[70, 60, 50, 40, 30, 20, 10]
"""
