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
b3=Book(300)
print(b1+b2+b3)

"""output-->The number of pages:600

in this program we get 600 as a output when control reach at print(b1+b2+b3)
whenever control see '+' operator it call __add__ method first of all b1+b2 calls
the __add__ method now b1+b2 return Book object again control raech at print(b1+b2+b3)
now result of (b1+b2)+b3 again call the __add__ method now book object + object
result is 600,we are priting result of refernce object now __str__ method is
calling and we get our result-->The number of pages:600"""
