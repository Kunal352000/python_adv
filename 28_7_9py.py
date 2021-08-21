from threading import Thread
def display():
    for i in range(10):
        print("Aiswariya")
t1=Thread(target=display)#creating a thread to execute display() fun
t1.start()#starting of thread
for i in range(10):
    print('Abhishek')
