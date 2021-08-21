from datetime import datatime
class test:
    """this class is developed by "kj" """
    def __init__(self):
        self.now=datatime.now()
    def __repr__(self):
        return "cdt is {}".format(self.now)
t1=test()
print(t1)
