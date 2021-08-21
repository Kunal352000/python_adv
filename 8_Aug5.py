"""
-->The thread execution is not under the programmer controller
-->The thread execution is under the control of job-schedular

What is job-sehedular?
======================
The job schedular is predefined application to scheduling the jobs execution
based on scheduling algorithims

how to suspend one thread execution temporary some time?
========================================================
we can suspend one thread exeution temporary some time by using sleep function
of time module
"""
import threading
print("Welcome")
import time
class x(threading.Thread):
    def run(self):
        for i in range(5):
            print("hey")
class y(threading.Thread):
    def run(self):
        time.sleep(10)
        for i in range(5):
            print("kunal")
t1=x()
t1.start()
t2=y()
t2.start()
for k in range(5):
    print("hello")
