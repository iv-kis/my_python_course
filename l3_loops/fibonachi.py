'''
Created on 29 июл. 2018 г.

@author: ivkis
'''
'''Фибоначи'''
import datetime
j=1
k=0
i=1
Fib_count=1
d=int(input('введите количество '))
print()
print('Фибоначи:')

#ms=datetime.datetime.now()
while Fib_count<=d:
    if i!=j+k:
        i+=1
        continue
    #delta=lambda x: datetime.datetime.now()-x
    print(i, end=' ') 
    #(',delta(ms).,' ms)
    #ms=datetime.datetime.now()
    temp=j
    j=j+k
    k=temp
    Fib_count+=1
    i+=1