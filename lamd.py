n=int(input("Enter n value: "))
for i in range(n):
    if i == n//2:
        for j in range(n,0,-1):
            print(j,end=" ")
        print()
    else:
        print("  "*(n//2)+ str(n-i))
