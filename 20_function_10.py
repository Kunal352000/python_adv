"""
create a function to return sum of given iterable object elements?
"""
obj=eval(input("Enter iterable object: "))
def my_sum(x):
    s=0
    for i in x:
        s+=i
    print(s)
my_sum(obj)
"""
output:
-------
Enter iterable object: (1,2,3,4,5)
15
"""
