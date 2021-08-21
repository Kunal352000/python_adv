from threading import *
def display():
    for i in range(10):
        print('Anushka thread executed by:',current_thread().getName())
t=Thread(target=display)#creating a thread to executing display()
t.start()#starting of a thread
for i in range(10):
    print('Virat thread executed by:',current_thread().getName())
