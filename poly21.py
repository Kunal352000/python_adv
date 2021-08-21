class x:
    def __init__(self,p,q):
        self.p=q
        self.q=q
    def add(self):
        print(self.p+self.q)
class y(x):
    def __init__(self,a,b):
        super().__init__(4,5)
        self.a=a
        self.b=b
    def sub(self):
        print(self.a-self.b)
y1=y(4,5)
y1.sub()
y1.add()
