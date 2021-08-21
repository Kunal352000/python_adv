from threading import*
def display1():
    for i in range(10):
        print('katrina thread executed by:',current_thread().getName())
def display2():
    for j in range(10):
        print("karenna thread executed by:",current_thread().getName())
def display3():
    for k in range(10):
        print("Raveena thread executed by:",current_thread().getName())
t1=Thread(target=display1)
t2=Thread(target=display2)
t3=Thread(target=display3)
t1.start()
t2.start()
t3.start()
for i in range(10):
    print('kunal thread executing by:',current_thread().getName())
