"""
mixing of both non-default and default argumnets"""
def add(x,y=2):#here x is non-default and y is default
    z=x+y
    print(z)
add(5,5)
add(6)
"""
output:
=======
10
8

we can mix non-default and deafult arguments but we cant mix default
and non-default"""
