"""
creat a function to return the minimum element from the given iterable object"""
obj=eval(input("Enter your iterable object: "))
def my_min(x):
    m=x[0]
    for i in x:
        if m>i:
            m=i
    print(m)
my_min(obj)
