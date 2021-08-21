class Book:
    def __init__(self,pages):
        self.pages=pages
b1=Book(100)
print(b1)
#<__main__.Book object at 0x0000023B88208FD0>

""" whenever we are priting refernce object internally __str__ method is executed

    if we are not creating __str__ method in class then refernece object is printed
    in the form of hashcode"""
