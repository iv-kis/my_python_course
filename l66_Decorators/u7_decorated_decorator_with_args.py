'''
Created on 16 авг. 2018 г.

@author: ivkis
'''
def decorator_with_args(decorator):
    def decorator_maker(*args,**kwargs):
        def wrapper(func):
            return decorator(func,*args,**kwargs)
        return wrapper
    return decorator_maker

@decorator_with_args
#создаём из исходного декоратора декоратор, умеющий принимать аргументы
def decorated_decorator(func, *args, **kwargs):
    #определяем исходный декоратор
    def wrapper(func_arg1, func_arg2):
        print("Мне передали...:",args,kwargs)
        return func(func_arg1, func_arg2)
    return wrapper
 
# Теперь декорируем любую нужную функцию нашим новеньким, ещё блестящим декоратором:
 
@decorated_decorator(42, 404)
def decorated_function(func_arg1, func_arg2):
    print("Привет,", func_arg1, func_arg2)
 
decorated_function("Вселенная и", "всё прочее")
