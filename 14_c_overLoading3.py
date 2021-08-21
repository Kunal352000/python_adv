class test:
    """Constructor overloading by defalt argument"""
    def __init__(self,a=None,b=None,c=None):
        print("constructor with 0|1|2|3")
t=test()

t=test(10)

t=test(10,20)

t=test(10,20,"k")
