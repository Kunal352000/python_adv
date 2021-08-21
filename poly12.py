class x:
    def __init__(self):
        print("i am in x class constructor")
class y(x):
    def __init__(self):
        print("i am in y class constructor")
        super().__init__()
y1=y()
""" in this senario we are reciving -->
i am in y class constructor
i am in x class constructor
bcoz we are using super()method"""
