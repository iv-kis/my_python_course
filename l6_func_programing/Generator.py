'''
Created on 6 авг. 2018 г.

@author: ivkis
'''

def generator(l):
    for i in range(l+1):
        yield i/2
        
#print(list(generator(int(input()))))

def simple_generator(val):
    val += 1
    while val > 0:
        val -= 1
        yield val
    return "stop: val={}".format(val)
        
gen_iter = simple_generator(5)
try:
    print(next(gen_iter))
    print(next(gen_iter))
    print(next(gen_iter))
    print(next(gen_iter))
    print(next(gen_iter))
    print(next(gen_iter)) 
    print(next(gen_iter)) #val=0
except StopIteration as e:
    print(e)
finally:
    print()
#####################
gen_iter = simple_generator(5)
for i in gen_iter:
    print(i,end=' ')
print('\n')
#####################
print([i for i in simple_generator(5)])
print(sum(i for i in simple_generator(5)))
####################
print()
from sys import getsizeof
my_comp = [x * 5 for x in range(1000)]
my_gen = (x * 5 for x in range(1000))
print(getsizeof(my_comp))
print(getsizeof(my_gen))
