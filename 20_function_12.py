"""create a function to return the minimum element from the given iterable obj"""
obj=eval(input("Enter your iterable object: "))
def my_min(x):
    m=x[0]
    for i in x:
        if m>i:
            m=i
    print(m)
my_min(obj)
"""
output:
-------

Enter your iterable object: "kunal"
a

Enter your iterable object: [78,90,12,43,8]
8
"""
