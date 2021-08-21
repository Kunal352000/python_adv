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
b4=Book(400)
print(b1+b2+b3+b4)

"""output--->The number of pages:1000


whenever control reach at print(b1+b2+b3+b4) then first immediatley b1+b2 call
__add__ method now result of b1+b2 is book object now again (b1+b2 book result)+ b3 book object
is calling __add__ method now (b1+b2)+b3 return 600 as a book object now again control raech at
print(b1+b2+b3+b4) now result of (b1+b2+b3)+b4 once again calling __add__ method now total is 1000
we are priting result of refernce object so __str__ method is calling and we get The number of pages:1000
as o/p

in this program 3 times __add__ method is executed and after this __str__ method is executed"""
