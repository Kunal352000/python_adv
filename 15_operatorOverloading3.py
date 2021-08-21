class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        return self.pages+other.pages
b1=Book(100)
b2=Book(200)
b3=Book(300)
print(b1+b2+b3)
"""TypeError: unsupported operand type(s) for +: 'int' and 'Book'


    b1+b2 return int data and our b3 contains object we are adding int + object
    that why we get error"""
