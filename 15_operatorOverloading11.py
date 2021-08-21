class Book:
    def __init__(self,pages):
        self.pages=pages
    def __str__(self):
        return 'The number of pages:'+str(self.pages)
b1=Book(100)
b2=Book(200)
b3=Book(300)
print(b1)
print(b2)
print(b3)
