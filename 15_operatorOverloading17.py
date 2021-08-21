class Book:
    def __init__(self,pages):
        self.pages=pages
    def __str__(self):
        return 'The number of pages:'+str(self.pages)
    def __add__(self,other):
        total=self.pages+other.pages
        b=Book(total)
        return b
b1=Book(100)
b2=Book(200)
print(b1)
print(b2)
print(b1+b2)
