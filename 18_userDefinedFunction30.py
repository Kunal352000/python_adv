def f1(*x,*y,**z):
    print(x,type(x))
    print(y,type(y))
    print(z,type(z))
f1(3.2,4,5j,False,name="kunal",age=21)
"""
output:-
--------
This program give invalid syntax becoz in parameter we are passing two *args
argumnet,passing two paramter is not sense at all
"""
