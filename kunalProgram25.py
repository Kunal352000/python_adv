n=int(input("Enter number of rows: "))
for i in range(n):
    print(" "*(n-1-i),end="")
    for j in range(i+1):
        print(j+1,end=" ")
    print()
for i in range(n-1):
    print(" "*(i+1),end="")
    for j in range(n-1-i):
        print(j+1,end=" ")
    print()
