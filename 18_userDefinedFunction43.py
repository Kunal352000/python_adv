"""
create a function to return absolute value of the given number
"""
num=eval(input("Enter the value: "))
def my_abs(x):
    if x>=0:
        return x
    else:
        return -(x)
print(my_abs(num))
"""
output:
-------
Enter the value: -444444
444444
"""
