"""
arbitary argumnets:
===================
    -->The arbitary argumnets takes 0 or more values
    -->by default arbitary argumnet type is tuple
     syntax:
             def fun name(*parameter):
                 ---------
                 ---------
                 ---------
"""
def f1(*args):
    print(args,type(args))
f1()

"""
output:
=======
() <class 'tuple'>

if we are not passing any value in arbitary argumnet then also our program
is executed and return type is empty tuple"""
