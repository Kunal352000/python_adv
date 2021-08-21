for row in range(7):
    for col in range(5):
        if (row==0 or row==6) and (col%4!=0):
            print("*",end=" ")
        elif col==0:
            print("*",end=" ")
        elif (row==1 or row==5) and col==4:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    
    
