class Book:
    def __init__(self,pages):
        self.pages=pages
    def __str__(self):
        return 'kunal'
b1=Book(100)
print(b1)

"""whenever we are printing refernce variable internally __str__ method is executed

    in __str__method we return 'kunal' as a string thats why 'kunal' is printing
    if we are not write __str__ method in class then it return hascode of that object"""
