from random import choices
from string import ascii_letters,digits
s=ascii_letters + '!@#$%^&*' + digits
num=int(input("Enter number of charcters: "))
print("".join(choices(s,k=num)))
