"""wap to generate 6-charcters arndom string?"""
from random import choice
from string import ascii_letters,digits
s=ascii_letters + '@#$&*!^' +digits
#print(s)
print(choice(s),choice(s),choice(s),choice(s),
      choice(s),choice(s),sep="")
