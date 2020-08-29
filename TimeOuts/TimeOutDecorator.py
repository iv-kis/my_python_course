'''
Created on 13 авг. 2018 г.

@author: ivkis
'''
import time
import os

#Firstly, you have to install pip and timeout decorator from pip via cmd 
#for Windows we have to redefine timeOut Decorator,
if os.name == 'nt':
    # We redefine timeout_decorator on windows
    class timeout_decorator:
        @staticmethod
        def timeout(*args, **kwargs):
            return lambda f: f #возвращает ничего не делающий декоратор (no-op)
else:
    import timeout_decorator #for os other than Windows

@timeout_decorator.timeout(5)
def mytest():
    print("Start")
    for i in range(1,10):
        time.sleep(1)
        print("{}d seconds have passed".format(i))

mytest()