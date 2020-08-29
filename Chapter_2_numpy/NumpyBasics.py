'''
Created on 13 окт. 2018 г.

@author: ivkis
'''
import numpy as np
a = np.array([[1,2,3],[2,4,6]], dtype=np.complex)
#print(a)

b=np.ones((2,3))
#print (b)

#print(np.eye(3))          #единичная матрица

#print(np.empty((2,3)))    #пустой массив

#print(np.arange(2.1))
#print(np.arange(0,1,0.2))
#print(np.linspace(0,1,3))

c=np.fromfunction(lambda i,j: i+j,(2,3))
#применяет функцию к индексам (индексы с нуля!)

#np.set_printoptions(precision=1, threshold=np.nan)
print(np.arange(0, 3000, 1))