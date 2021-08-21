n=int(input("Enter n value: "))
for i in range(n):
    if i==n//2:
        print(i+1,end="")
    else:
        print("  "*(n//2)+str(i+1))
