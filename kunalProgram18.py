n=int(input("Enter no of rows: "))
for i in range(n):
    print(" "*i,end="")
    for j in range(n-i):
        print(j+1,end=" ")
    print()
