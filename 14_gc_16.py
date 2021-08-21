import sys
class test:
    def __init__(self):
        print("i am in constrcutor")
    def __del__(self):
        print("i am in destructor")
t1=test()
print(sys.getrefcount(t1))#2
t2=t1
print(sys.getrefcount(t2))#3
t3=t2
print(sys.getrefcount(t3))#4
t4=test()
print(sys.getrefcount(t4))#2
del t3
print(sys.getrefcount(t1))#3
del t2
print(sys.getrefcount(t1))#2
del t1
print("bye")
