n=int(input("Enter number of rows: "))
for i in range(n):
    print(" "*i,end="")
    for j in range(n-i):
        print(n-j,end=" ")
    print()
