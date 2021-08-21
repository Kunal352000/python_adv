class Book:
    def __init__(self,pages):
        self.pages=pages
    def __str__(self):
        return "The number of pages:"+str(self.pages)
b1=Book(100)
b2=Book(200)
print(b1)
print(b2)
"""
output--->
The number of pages:100
The number of pages:200

"""
