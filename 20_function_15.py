"""create a function to return element in desending order from the given
iterable object"""
obj=eval(input("Enter the iterable object: "))
def my_desec_ord(x):
    for i in range(len(x)):
        for j in range(i+1,len(x)):
            if x[i]<x[j]:
                x[i],x[j]=x[j],x[i]
    print(x)
my_desec_ord(obj)
"""
output:

Enter the iterable object: [1,2,3,4,5,6,7]
[7, 6, 5, 4, 3, 2, 1]
"""
