"""
mixing of both normal argumnet and arbitary argumnet
"""
def f1(x,*y):
    print(x,type(x))
    print(y,type(y))
f1()

"""
output:
=======
TypeError: f1() missing 1 required positional argument: 'x'

we recive output as error becoz we are not passing value to the x,passing value
to the normal argumnet is manditory but passing value to the arbitary argumnet
is not manditory
"""
