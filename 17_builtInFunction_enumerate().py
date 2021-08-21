"""
enumerate()-->to return enumerate object,it contains tuple's of index and element
            from the given iterable object
           --> if we want to retrive index and element from the given iterable
           object in that case we are using enumerate()
           --> enumerate(iterableobject,start=0)"""
x=[3,2,4,5j,False,"kunal"]
for i in range(len(x)):
    print(i,x[i])
