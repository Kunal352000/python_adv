n=int(input("Enter number of rows: "))
for i in range(n):
    print(" "*(n-1-i)+(str(i+1)+' ')*(i+1))
for i in range(n-1):
    print(" "*(i+1)+(str(n-1-i)+' ')*(n-1-i))
