def f1(*x,y,**z):
    print(x,type(x))
    print(y,type(y))
    print(z,type(z))
f1(y=9,3.2,4j,False,name="kunal",age=21)
"""
output:POSTIONAL ARGUMNET FOLLOW KEWYWORD ARGUMNET

THIS IS NOT POSSIBLE -->CALIING NORMAL ARGUMNET IN FIRST WHEN AT THE TIME OF
FUNCTION DEFINATION WE ARE DEFINING *ARGS ARUMENT FIRST
"""
