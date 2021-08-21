num=int(input("Enter your number: "))
def my_fact(x):
    if x==0:
        return 1
    else:
        return x*my_fact(x-1)
for i in range(num+1):
    res=my_fact(i)
    print("the factorial of {} is {}".format(i,res))
