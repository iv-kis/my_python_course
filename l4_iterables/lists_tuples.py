'''
Created on 29 июл. 2018 г.

@author: ivkis
'''

#В случае, если вы выполните простое присвоение списков друг другу,
# то переменной b будет присвоена ссылка на тот же элемент данных в памяти, на который ссылается a,
#  а не копия списка а. Т.е. если вы будете изменять список a, то и b тоже будет меняться.
'''
a = [1, 3, 5, 7]
b = list(a) #создание копии списка
c=b.copy() #создание копии списка
d=c[:] #создание копии списка
print(a)
print(b)
a[0] = 10
print(a)
print(b) 
print(c) 
print(d)
'''
'''
b = a #b и a ссылаются на один и тот же объект
print(a)
print(b)
a[0] = 3
print(a)
print(b)
'''
'''
a = [1, 3, 5, 7]
a.append(5)
print(a)

a.remove(5)
print(a)
print(a[3])
print(a[-3])
del a[3]
print(a)
print()
l = [1, 3, 2, 5, 7]
l.sort()
print(l)
l = l.sort() #результат выполнения не нужно записывать в эту переменную, т.к. методы списков, в отличие от строковых методов, изменяют сам список 
print(l) #печатает пустоту, т.к. метод sort ничего не возвращает
'''
'''
#зачем нужна звёздочка
def func2 (x, y, z):                
    print (x, y, 'and', z)
def func1 (A, B):
    if A == 'key':
        return func2(*B)

func1('key', ['a', 'b', 'c'])

a=[1 for i in range(5)]
b=[2 for i in range(3)]
a.extend(b)
print(a)

'''
#преобразование кортежа в список и обратно 
words=("spam","eggs","sausages")
print(words)
try:
    words[0]="cheese"
except:
    print("TypeError: 'tuple' object does not support item assignment")
finally:
    l=list(words)
    l[0]="cheese"
    words=tuple(l)
    print(words)


























