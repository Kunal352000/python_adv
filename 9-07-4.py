class test:
    def __init__(self):
        print("i am in constructor.")
    def __del__(self):
        print("i am in destructor.")
t1=test()
t2=test()
t3=test()
del t2
print("bye")
