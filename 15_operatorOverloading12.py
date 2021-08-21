class Book:
    def __init__(self,pages):
        self.pages=pages
    def __str__(self):
        return 'The number of pages:'+str(self.pages)
    def __add__(self,other):
        return self.pages+other.pages
b1=Book(100)
b2=Book(200)
b3=Book(300)
#print(b1+b2)
#print(b3+b1)
print(b1+b2+b3)
"""
output---->TypeError: unsupported operand type(s) for +: 'int' and 'Book'

    in this program we get error becoz when control reach at print(b1+b2+b3)
    then immediatley b1+b2 call __add__ method only b1+b2 executed and return
    output as a form of int now b1+b2 result is int and our b3 contain 'book object'
    now (b1+b2 result)+b3 again calling __add__ method in python 'int'+'object'
    is not expected thats why we get error
    """
