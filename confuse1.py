class test:
    def __init__(self):
        print("constructor")
    def __del__(self):
        print("destructor")
t1=test()
print("'end'")
