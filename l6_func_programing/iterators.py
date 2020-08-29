'''
Created on 16 авг. 2018 г.

@author: ivkis
'''
import itertools

class MyIterator:
    def __init__(self,n):
        self.max=n
        self.counter=0
    def __next__(self):
        if self.counter<self.max:
            self.counter+=1
            return self.counter
        else:
            raise StopIteration
    def __iter__(self):
        return self
##########################
class Fibonacci: 
#Итератор последовательности Фибоначчи до N
    def __init__(self, N): 
        self.a=0
        self.b=1
        self.counter=0
        self.max=N
    def __iter__(self): 
    # сами себе итератор: в классе есть метод next() 
        return self 
    def __next__(self): 
        if self.counter < self.max: 
            a,self.a,self.b,self.counter=self.a,self.b,self.a+self.b,self.counter+1
            return a 
        else: 
            raise StopIteration 
        
# Использование: 
for i in Fibonacci(20): 
    print(i,end=" ")
print()
############################

new_iter1=MyIterator(3)
for i in new_iter1:
    print(i)
print()
############################
def getSimple(state=[]): 
    if len(state) < 4: 
        state.append("")
        return state
    else:
        print("end")

new_iter2 = iter(getSimple, None) 
for i in new_iter2:
    print(i)   
print()
######################### 
print('sorted():',sorted('54321'))    
print('enumerate():',[i for i in enumerate('abcde')])
print()
##########################
it1 = iter([1,2,3]) 
it2 = iter([8,9,0]) 
print('itertools.chain():',end='')
for i in itertools.chain(it1, it2):
    print(i,end=' ')
print()
##########################
for i in itertools.count(1): 
    if i > 40: 
        break
    print(i,end=' ')
print()
##########################
for i in itertools.takewhile(lambda x: x > 0, [1, -2, 3, -3]): 
    print(i,end=' ') 
print()
for i in itertools.dropwhile(lambda x: x > 0, [1, -2, 3, -3]): 
    print(i,end=' ')
##########################
