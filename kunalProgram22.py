n=int(input("Enter number of rows: "))
for i in range(n):
    print(" "*(n-1-i)+ '* '*(i+1))
for j in range(n-1):
    print(" "*(j+1)+ '* '*(n-1-j))
