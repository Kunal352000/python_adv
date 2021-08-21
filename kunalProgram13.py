n=int(input("Enter no of rows: "))
for i in range(n):
    for j in range(n-i):
        print(n-j,end=" ")
    print()
