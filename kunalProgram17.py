n=int(input("Enter number of rows: "))
for i in range(n):
    print(" "*i + (chr(65+i)+' ')*(n-i))
    
