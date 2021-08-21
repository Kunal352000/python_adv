"""to get the object count"""
import sys
class test:
    def m1(self):
        pass
t1=test()
print(sys.getrefcount(t1))#2
t2=t1
print(sys.getrefcount(t1))#3
del t2
print(sys.getrefcount(t1))#2
