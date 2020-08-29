'''
Created on 29 июл. 2018 г.

@author: ivkis
'''
from datetime import datetime
from datetime import timedelta
from time import sleep

for i in range(20):
    start = datetime.now()
    sleep(0.001)
    end = datetime.now()
    print((end - start).microseconds,end=' ')

