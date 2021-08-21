"""
mixing of both arbitary argumnet and normal argumnet
"""
def f1(*x,y):
    print(x,type(x))
    print(y,type(y))
f1(2.3,4j,True,"kunal")

"""
output
------
TypeError: f1() missing 1 required keyword-only argument: 'y'

we get error becoz all values are passed to *x(arbitary argumnet) in the form
of tuple and out y(normal argumnet) is empty
"""
