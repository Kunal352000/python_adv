"""wap to implement simple dice game"""
from random import randint
roll_up=randint(1,6)
choice=int(input("Enter your choice: "))
if choice>0 and choice<=6:
    print("Dice value is",roll_up)
    if choice==roll_up:
        print("congrats you are win the game")
    else:
        print("sorry you lose the game")
else:
    print("Enter b/w 1-6")
