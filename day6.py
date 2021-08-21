r=int(input())
for i in range(r):
    strr=input()
    strList=list(strr)

    for i in range(len(strList)):
        if i%2==0:
            print(strList[i],end="")
    print(" ",end="")

    for i in range(len(strList)):
        if i%2!=0:
            print(strList[i],end="")
    print()
    
