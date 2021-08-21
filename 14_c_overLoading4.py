class test:
    """Constructor overloading by variable length"""
    def __init__(self,*a):
        print("constructor with n number of arguments")
t=test()

t=test(10)

t=test(10,20)

t=test(10,20,"k")
