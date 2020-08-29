'''
Created on 24 июл. 2018 г.

@author: ivkis
'''
for i in 'Привет Мир':
    print(i * 2, end='')
print()
for i in range(11):
    if i%2==0:
        continue
    print(round(i*0.1,1), end=' ')
print()
print(i)


