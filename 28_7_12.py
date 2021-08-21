from threading import*
def display():
    for i in range(10):
        print("Anushka Thread executed by:",current_thread().getName())
t=Thread(target=display)#creating a thread to execute display() function

for i in range(10):
    print('Virat Thread executed by:',current_thread().getName())
t.start()
