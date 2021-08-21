import time
class test:
    def __init__(self):
        print("constructor")
    def __del__(self):
        print("destrcutor")
t1=test()
time.sleep(5)
print("End")
    
