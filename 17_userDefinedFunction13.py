def f1(*args):
    print(args,type(args))
f1(2,3.11,False,5j,"kunal")

"""
output
======
(2, 3.11, False, 5j, 'kunal') <class 'tuple'>

in arbitary argumnet we can pass hetrogenious element also
"""
