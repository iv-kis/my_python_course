'''
Created on 5 авг. 2018 г.

@author: ivkis
'''

# обращение числа. Две возможные ошибки при вводе: 0 и не число

'''def division(): 
    try:
        print('Введите число:', end=' ')
        k = 1/float(input())
    except ZeroDivisionError as zde: #создание объекта zde класса ZeroDivisionError
        print('деление на ноль'+'|'+str(zde))
        division()
    except ValueError:
        print('вы не ввели число')
        division()
    else:
        print(k)
        print('программа завершена')
print('Программа выводит 1/x')
division()

'''#################################
#подстановка текста ошибки в общее сообщение
'''
print("start")
try:
    val = int(input("input number: "))
    tmp = 10 / val
    print(tmp)
except Exception as e:
    print("Ошибка! {0}{1}".format(e,' text'))
print("stop")
'''
############################
#создание собственного класса ошибки
class NegValException(Exception):
    pass

try:
    val = int(input("input positive number: "))
    if val < 0:
        raise NegValException("Neg val: "+str(val))
    print(val * 10)
except NegValException as e:
    print(str(e))
  
    
    
    
    