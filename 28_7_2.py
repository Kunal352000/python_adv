"""
how to activate a thread:
-------------------------
    we can activate the thread by calling run() logic through the start() of a
    Thread class of threadig module
"""
import threading
print("Welcome")
class test(threading.Thread):
    def run(self):
        for i in range(5):
            print("hey")
t1=test()
t1.start()
for j in range(5):
    print("hello")
