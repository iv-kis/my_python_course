'''
Created on 13 окт. 2018 г.

@author: ivkis
'''
import numpy as np
a=np.array([[20,30,40,50],[1,2,3,4]])
b=np.arange(4)
#print(a*b)
#print(b*10)
#print(np.sum(b))
#print(np.max(a))
#print(a.max())
#print(a.sum(axis=0))
#for el in a.flat:
#    print(el,end=" ")
#print()

print(a.shape) 
b=a.ravel()
print(b, b.shape)
#print(a)
c=b.reshape(4,2)
print(c)
print(c.transpose())

a.resize((4,2)) #изменяет сам массив!
print(a)