'''
Created on 13 авг. 2018 г.

@author: ivkis
'''
from multiprocessing import Process
import time
 
def do_actions():
    #Function that should timeout after 5 seconds. It simply prints a number and waits 1 second.
    i = 0
    while True:
        i += 1
        print(i)
        time.sleep(1)
 
if __name__ == '__main__':
    # We create a Process
    action_process = Process(target=do_actions)
 
    # We start the process and we block for 5 seconds.
    action_process.start()
    action_process.join(timeout=int(input("Введите таймаут")))
 
    # We terminate the process.
    action_process.terminate()
    print("TimeOut!")