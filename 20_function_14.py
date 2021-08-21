"""create a function to return the elements in ascending order"""
obj=eval(input("Enter iterable object: "))
def my_asc_num(x):
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if x[i]>x[j]:
                x[i],x[j]=x[j],x[i]
    print(x)
my_asc_num(obj)
"""
output:
-------
Enter iterable object: [34,56,78,98,99,96]
[34, 56, 78, 96, 98, 99]
"""
