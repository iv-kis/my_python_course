'''
Created on 6 авг. 2018 г.

@author: ivkis
'''
#even=[2*i for i in range(10**100)]

# способ 1
import threading

# Register a handler for the timeout
def TO_handler():
    print("Timeout Error!")  
 
t=threading.Timer(5,TO_handler)
t.start()
even=[2*i for i in range(10**100) if t.is_alive()]

#программа продолжает работать и перебирать i, но после истечения таймера t.is_alive()=False, и список дальше не заполняется, т.е. память не забивается
#чтобы остановить программу, для создания списка нужен генератор, в котором можно ввести проверку и break

    


    