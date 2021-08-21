import sys
class test:
    def __init__(self):
        print("i am in constructor")
    def __del__(self):
        print("i am in destructor")
t1=test()
print(sys.getrefcount(t1))#2 t1 and self
t2=t1
print(sys.getrefcount(t2))#2from t1 and 1 from t2-->3
t3=t2
print(sys.getrefcount(t3))#3 from t2 and 1 from t3-->4
print("*"*29)
t4=test()
print(sys.getrefcount(t4))#2 bcoz we are creating new object
del t3
print(sys.getrefcount(t1))#3
del t2
print(sys.getrefcount(t1))#2
del t1
print("bye")
