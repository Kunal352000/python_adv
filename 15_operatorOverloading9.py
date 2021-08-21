class Book:
    def __init__(self,pages):
        self.pages=pages
    def __str__(self):
        return "The number of pages:"+ self.pages
b1=Book(100)
print(b1)
b2=Book(200)
print(b2)

"""
output: TypeError: can only concatenate str (not "int") to str

in this program our recuriment is to print str message and pages but we get
error becoz we are adding string + integer if we want to display our o/p
we can convert out int into str like---> str(self.pages)"""
