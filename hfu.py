for row in range(7):
    for col in range(5):
        if col==0:
            print("*",end=" ")
        elif col==4 and (row%6==0):
            print("*",end=" ")
        elif col==3 and (row==1 or row==5):
            print("*",end=" ")
        elif col==2 and (row==2 or row==4):
            print("*",end=" ")
        elif row==3 and col==1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
