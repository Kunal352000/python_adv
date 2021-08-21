for row in range(7):
    for col in range(5):
        if row%6==0 and (col%4!=0):
            print("*",end=" ")
        elif(row in range(1,6)) and col%4==0:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
