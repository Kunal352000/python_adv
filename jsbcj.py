n=int(input("Enter n value: "))
for i in range(n):
    print("  "*i,end="")
    print("*",end=" ")
    if i!=n-1:
        print("  "*(2*n-2*i-3),end="")
        print("*",end=" ")
    print()
    
