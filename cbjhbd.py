n=int(input("engeeyg: "))
for i in range(n):
    if i==n//2:
        print("* "*n)
    else:
        print("  "*(n-3)+"*")
