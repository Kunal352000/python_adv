class test:
    """this class is developed by "kj" """
    def __init__(self,name):
        self.name=name
    def __repr__(self):
        return "hello %s"%self.name
t1=test("kunal")
print(t1)
