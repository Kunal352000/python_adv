class x:
    a=10
class y:
    a=15
class z(x,y):
    pass
print(z.a)
"""Output is a=10 becoz priority is left to right and in class x the value of a=10"""
