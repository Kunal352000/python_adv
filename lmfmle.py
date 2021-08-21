for row in range(7):
    for col in range(5):
        if col==0:
            print("*",end=" ")
        elif(row==0 or row==3) and (col%4!=0):
            print("*",end=" ")
        elif(row==1 or row==2) and (col==4):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
        
