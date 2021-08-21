import threading
print("Welcome")
class test(threading.Thread):
    def run(self):
        for i in range(5):
            print("hai")
t1=test()
t1.start()
for j in range(5):
    print("Hello")
