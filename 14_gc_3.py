import time
class test:
    def __init__(self):
        print("object initialization")
    def __del__(self):
        print("fulfilling last wish and perform cleanup activity")
t1=test()
t1=None
time.sleep(10)
print("End of appplication")
