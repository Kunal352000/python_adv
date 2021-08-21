class test:
    def __init__(self,name):
        self.name=name    
    def __add__(self,other):
        return self.name+other
    def __mul__(self,other):
        return self.name*other
    def __eq__(self,other):
        return self.name==other    
    def __contains__(self,other):
        return other in self.name
t1=test("siva")
