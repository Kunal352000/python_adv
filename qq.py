for row in range(7):
    for col in range(5):
        if row==0 or row==3 or row==6:
            print("*",end=" ")
        elif col==0 and row%3!=0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
