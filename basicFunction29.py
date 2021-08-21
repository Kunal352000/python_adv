def isEven(x):
    if x%2==0:
        return True
    else:
        return False
l=[0,5,10,15,20,25,30]
print(list(filter(isEven,l)))

l1=[0,5,10,15,20,25,30,35,40]
print(list(filter(lambda x:x%2==0,l1)))
