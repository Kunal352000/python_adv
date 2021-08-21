for row in range(7):
    for col in range(5):
        if row==0:
            print("*",end=" ")
        elif col==2 and (row!=6 and row!=0):
            print("*",end=" ")
        elif col==0 and (row==5):
            print("*",end=" ")
        elif row==6 and col==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
