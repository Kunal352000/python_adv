import time
class Test:
    def __init__(self):
        print("object Initalization")
    def __del__(self):
        print("fulfilling last wish and performing cleanup activity")
t1=Test()
t1=None
time.sleep(10)
print("End of application")
