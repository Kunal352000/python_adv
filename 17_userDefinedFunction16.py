"""
mixing of both normal argumnet and arbitary argumnet
"""
def f1(x,*y):
    print(x,type(x))
    print(y,type(y))
f1(5)
"""
output:
=======
5 <class 'int'>
() <class 'tuple'>

passing value to the normal argumnet is compulsory but passing value to the
arbitary argument is not compiulsory
"""

