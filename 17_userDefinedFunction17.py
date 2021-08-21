"""
mixing of both normal argumnet and arbitary argumnet
"""
def f1(x,*y):
    print(x,type(x))
    print(y,type(y))
f1(4,4.44,5j,True,'kunal')

"""
output:
=======
4 <class 'int'>
(4.44, 5j, True, 'kunal') <class 'tuple'>

in this above example first value is passing to the normal argumnet
and rest  of the other value is passing to the arbitary argumnet in the
form of tuple
"""
