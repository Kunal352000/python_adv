class x:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        print(self.a+self.b)
class y(x):
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def sub(self):
        print(self.a-self.b)
y1=y(2,3)
y1.sub()
y1.add()
y1.sub()
