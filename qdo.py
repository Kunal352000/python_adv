n=int(input("Enter n value: "))
for i in range(n):
    print("  "*(n-1-i),end=" ")
    print(i+1,end=" ")
    if i>=1:
        print((2*i-1)*"  ",end="")
        print(i+1,end="")
    print()
