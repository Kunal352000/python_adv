n=int(input("Enter number of rows: "))
for i in range(n):
    print(" "*i,end="")
    for j in range(n-i):
        print(chr(64+n-j),end=" ")
    print()
