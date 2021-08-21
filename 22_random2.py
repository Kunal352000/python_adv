"""
wap to generate random numbers based on user requirement"""
from random import randint
num=int(input("Enter no.of. digits: "))
for i in range(num):
    print(randint(0,9),end="")
"""
output:
--------
66783
"""
