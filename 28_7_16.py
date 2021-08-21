from threading import *
def display(name):
    for i in range(10):
        print(f'{name} thread executing by:',current_thread().getName())
t1=Thread(target=display,args=('katrina',))
t2=Thread(target=display,args=('deepicka',))
t3=Thread(target=display,args=('nora',))
t1.start()
t2.start()
t3.start()
for i in range(10):
    print('kunal thread executing by:',current_thread().getName())
