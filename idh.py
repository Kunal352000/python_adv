n=int(input("Enter n value: "))
for i in range(n):
    if i==0:
        print((str(i+1)+' ')*n)
    elif i==n-1:
        print((str(n)+' ')*n)
    else:
        print(str(i+1)+' ' + "  "*(n-2)+str(i+1))
