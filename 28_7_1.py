import threading
print("Welcome")
class test(threading.Thread):
    def run(self):
        for i in range(5):
            print("hey")
t1=test()
t1.run()
for j in range(5):
    print("hello")
"""
Welcome
hey
hey
hey
hey
hey
hello
hello
hello
hello
hello

in this above example we are creating a thread but it is not activated

"""
