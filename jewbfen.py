n=int(input("Enter n value: "))
for i in range(n):
    print("  "*i,end=" ")
    print("*"*(i+1),end=" ")
    if i != n-1:
        print("  "*((2*n)-(2*i)-3),end=" ")
        print("*"*(i+1),end=" ")
    print()
