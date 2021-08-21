class Book:
    def __init__(self,pages):
        self.pages=pages
    def __add__(self,other):
        total=self.pages+other.pages
        t=Book(total)
        return t
b1=Book(100)
b2=Book(200)
print(b1)
print(b2)
print(b1+b2)

"""Output-->
<__main__.Book object at 0x0000020B43428FD0>
<__main__.Book object at 0x0000020B434DABE0>
<__main__.Book object at 0x0000020B434DA910>
"""
