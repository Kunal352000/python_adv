class Book:
    def __init__(self,pages):
        self.pages=pages
    def __str__(self):
        return 'kunal'
    def __add__(self,other):
        total=self.pages+other.pages
        b=Book(total)
        return b
b1=Book(100)
b2=Book(200)
b3=Book(300)
print(b1)
print(b2)
print(b1+b2+b3)
"""output--> kunal
             kunal
             kunal
 in this program we get o/p as three time kunal,
 the result of b1+b2+b3 is 600 now we are priting refernce object
 whenever we are priting refernce object then immediatly __str__ method is executed
 and in __str__ method it return 'kunal' thats why we get third time also kunal"""
