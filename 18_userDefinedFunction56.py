"""
Function recursion:-function recursion means function can call itself
is called function recursion
"""
num=int(input("Enter your number: "))
def my_fact(x):
    if x==0:
        return 1
    else:
        return x*my_fact(x-1)
res=my_fact(num)
print("factrial of {} is {}".format(num,res))
