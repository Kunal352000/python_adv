from threading import *
import time
def display():
    time.sleep(2)
    for i in range(10):
        print('Anushka Thread executed by:',current_thread().getName())
t=Thread(target=display)#creating a thread to execute display function
t.start()#starting a thread
for i in range(10):
    print(10/0)
    print('Virat thread executed by:',current_thread().getName())
