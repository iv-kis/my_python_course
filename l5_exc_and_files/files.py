'''
Created on 5 авг. 2018 г.

@author: ivkis
'''

import os
filename=input('введите имя файла\n')
path=os.path.join(os.getcwd(),filename)
print(path)

#f=open(path,"w")                                   #убеждаемся на примере, что открытие в режиме "w" удаляет содержимое! 
#f.close
try:
    with open(path,"w+",encoding='UTF-8') as f:     #открываем файл для записи (создание нового файла)+чтение; выставляем кодировку
        f.write(input('введите строку 1\n')+'\n')
 #      raise Exception                             #чтобы проверить, закрывается ли файл в случае исключения   
        f.write(input('введите строку 2\n'))
        f.seek(0)                                   #ставим курсор в начало файла
        for l in f:
            print(l)
finally:
    print('\nФайл закрыт? ',f.closed)               #убеждаемся, что конструкция with ... as закрывает файл после работы, даже в случае исключения
