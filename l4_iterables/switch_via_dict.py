'''
Created on 5 авг. 2018 г.

@author: ivkis
'''
class ServiceException(Exception):
    pass

class SystemServiceException(ServiceException):
    pass

class BusinessServiceException(ServiceException):
    pass

#Аналог Switch-Case с помощью словаря:
def case1():
    raise BusinessServiceException('Business Service Exception')
def case2():
    raise ServiceException('Service Exception')
def case3():
    raise Exception('Exception')
select={                            #создаём словарь
        "1": case1,                 #передаём ключи, а НЕ САМИ ФУНКЦИИ, иначе они будут вызываться при создании словаря
        "2": case2,
        "3": case3
        }
try:
    func=select[input()]            #получаем ключ
    func()                          #вызываем функцию по ключу

#Располагаем except'ы в порядке наследования от дочернего к родительскому:
except KeyError:
    print("Success!")
except BusinessServiceException as BSE:
    print('BSE: {0}'.format(BSE))
    #try:
       # raise ServiceException('Service Exception')
    #except ServiceException as SE:
      #  print(str(SE))
except ServiceException as SE:
    print('SE: {0}'.format(SE))
except Exception as E:
    print('E: {0}'.format(E))


