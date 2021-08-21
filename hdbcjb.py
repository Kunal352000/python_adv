for row in range(7):
    for col in range(5):
        if (row in range(0,6)) and col%4==0:
            print("*",end=" ")
        elif row==6 and (col%4!=0):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
