class test:
    def __init__(self):
        self.a=10
        self.b=20
        self.c=30

t1=test()
del t1.a
t2=test()
del t2.b
print(t1.__dict__)
print(t2.__dict__)


