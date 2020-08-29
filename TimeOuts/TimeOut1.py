'''
Created on 6 авг. 2018 г.

@author: ivkis
'''
#even=[2*i for i in range(10**100)]
#способ 1
import threading
import time

# Register a handler for the timeout
def TO_handler():
    print("\nTimeout!")
   
def loop_forever(b):
    i=1
    print('start')
    while b.is_alive():
        time.sleep(1)
        print("{} seconds have passed".format(i))
        i+=1
    print('stop')                       

t=threading.Timer(int(input('Введите таймаут')),TO_handler) #после окончания таймера поток прерывается, t.is_alive=False
t.start()  
loop_forever(t)

#Создавать исключение для таймаута бесполезно, т.к. обрабатываются в разных потоках (?) 