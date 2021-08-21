"""
zip()-->the zip() to return the zip object
     -->zip(*iterableobj)
     -->the zip()is used to combine the elements from multiple iterable object
     """
eid=[1,2,3,4]
enames=["kunal","shivam","dhoni","virat"]
sal=[10000,20000,30000,40000]
dno=[10,20,30,40]
x=zip(eid,enames,sal,dno)
print(x)#return zip object
print(type(x))
print("*"*20)
for i in x:#if we want to retrive one by one value we use for loop
    print(i)
print("*"*20)
print(list(zip(eid,enames,sal,dno)))
print('*'*20)
print(dict(zip(eid,enames)))
print("*"*30)
print(set(zip(eid,enames,sal,dno)))
