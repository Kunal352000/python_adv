import time
class test:
    def __init__(self):
        print("object initialization")
    def __del__(self):
        print("fulfilling last wish and performing cleanup acitivity")
t1=test()
time.sleep(10)
print("End of application")
