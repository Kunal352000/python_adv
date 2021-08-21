"""
mixing of both arbitary argumnet and normal argumnet
"""
def f1(*x,y):
    print(x,type(x))
    print(y,type(y))
f1(2.3,4j,True,"kunal",y=111)

"""
output:
=======
(2.3, 4j, True, 'kunal') <class 'tuple'>
111 <class 'int'>

in this above example we didnt get error becoz we pass y value at the time of
function calling
"""
