from random import choice
from string import ascii_letters,digits
s=ascii_letters + '!@#$%^&*' + digits
num=int(input("Enter the no.of charcters: "))
for i in range(num):
    print(choice(s),end="")
