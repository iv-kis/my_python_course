'''
Created on 1 авг. 2018 г.

@author: ivkis
'''
a = set()
print(a)
a = set('hello')
print(a)
a = {i ** 2 for i in range(10)} # генератор множеств

a=[1 for i in range(5)]
b=[2 for i in range(3)]
a.extend(b)
a=list(set(a))
print(a)