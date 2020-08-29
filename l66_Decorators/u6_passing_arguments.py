'''
Created on 16 авг. 2018 г.

@author: ivkis
'''
def a_decorator_passing_arguments(function_to_decorate):
    def a_wrapper_accepting_arguments(*args): # аргументы прибывают отсюда
        print("Смотри, что я получил:",args)
        function_to_decorate(*args)
    return a_wrapper_accepting_arguments
 
# Теперь, когда мы вызываем функцию, которую возвращает декоратор,
# мы вызываем её "обёртку", передаём ей аргументы и уже в свою очередь
# она передаёт их декорируемой функции
 
@a_decorator_passing_arguments
def print_full_name(*args):
    print("Меня зовут"," ".join(args))
    
if __name__ == '__main__': 
    print_full_name('Жан',"Клод","ван","Дамм")



