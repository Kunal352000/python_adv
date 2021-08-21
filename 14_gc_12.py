import time
class test:
    def __init__(self):
        print("object initialization")
    def __del__(self):
        print("fulfilling last wish and performing cleaup activities.")
list=[test(),test(),test()]
time.sleep(10)
list=None
time.sleep(10)
print("End of application")

