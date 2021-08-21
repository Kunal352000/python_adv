import time
class Test:
    def __init__(self):
        print("object initizalization")
    def __del__(self):
        print("fulfilling last wish and performing cleaup activity:")
t1=Test()
del t1
print(t1)
