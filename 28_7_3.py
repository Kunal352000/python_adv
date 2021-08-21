import threading
print("welcome")
class x(threading.Thread):
    def run(self):
        for i in range(5):
            print("hai")
class y(threading.Thread):
    def run(self):
        for i in range(5):
            print("kunal")
t1=x()
t1.start()
t2=y()
t2.start()
for j in range(5):
    print("hello")
