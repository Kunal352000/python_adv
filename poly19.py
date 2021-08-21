class x:
    def __init__(self,a,b):
        self.p=p
        self.q=q
    def add(self):
        print(self.p+self.q)
class y(x):
    def __init__(self,c,d):
        self.p=c
        self.q=d
    def sub(self):
        print(self.p-self.q)
y1=y(2,3)
y1.sub()
y1.add()


