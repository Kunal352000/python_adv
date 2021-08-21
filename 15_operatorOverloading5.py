class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):#in this if we are passing 3 arg we get error only 2 arg is legal
        return self.pages+other.pages
b1=Book(100)
b2=Book(200)
print(b1+b2)
