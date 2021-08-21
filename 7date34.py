class test:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30

    def delete(self):
        del self.b
        del self.c
t1=test()
t1.delete()
print(t1.__dict__)
del t1.a
print(t1.__dict__)
