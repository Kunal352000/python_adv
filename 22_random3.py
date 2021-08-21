"""wap to implement simple dice game"""
from random import randint
roll_up=randint(1,6)
choice=int(input("Enter the number: "))
print("Dice face value is:",roll_up)
if choice==roll_up:
    print("winnner")
else:
    print("looser")
