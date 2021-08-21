import sys
class test:
    def __init__(self):
        print("object initialization")
t1=test()
t2=t1
t3=t2
t4=t3
print(sys.getrefcount(t1))#5
