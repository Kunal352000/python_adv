import time
class test:
    def __init__(self):
        print("object initizalization")
    def __del__(self):
        print("fulfilling last wish and performing cleanup activity")
t1=test()
t1=None
print(t1)
