'''
Created on 1 авг. 2018 г.

@author: ivkis
'''
func = lambda x, y: x + y
print(func(1, 2))
print(func('a', 'b'))
print((lambda x, y: x + y)(1, 2))
print((lambda x, y: x + y)('a', 'b'))

def func(**dic):
    return dic

print(func(a=1, b=2, c=3))
print(func())
print(func(a='python'))

def fibb(n):
    if n>35:
        return('слишком большое число!')
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibb(n-1) + fibb(n-2)
print(fibb(int(input("введите номер числа Фибоначчи"))))