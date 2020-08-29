'''
Created on 23 июл. 2018 г.

@author: ivkis
'''
if __name__ == "__main__":
    a=4
    b=5
    print("a: id ",id(a),"value ",a)
    print("b: id ",id(b),"value ",b)
    a=b
    print("a=b")
    print("a: id ",id(a),"value ",a)
    print("b: id ",id(b),"value ",b)

    print("\nпро списки:")

#В случае, если вы выполните простое присвоение списков друг другу,
# то переменной b будет присвоена ссылка на тот же элемент данных в памяти, на который ссылается a,
#  а не копия списка а. Т.е. если вы будете изменять список a, то и b тоже будет меняться.

    list_a = [1, 3, 5, 7]
    list_b = list(list_a) #создание копии списка
    list_c=list_b.copy() #создание копии списка
    list_d=list_c[:] #создание копии списка
    print("a:",list_a)
    print("b:",list_b)
    print("c:",list_c)
    print("d:",list_d)
    print('присваиваем списку list_b значение list_a')
    print('присваиваем 1-му элементу списка list_а значение 10')
    list_b=list_a
    list_a[0] = 10
    print("a:",list_a)
    print("b:",list_b) 
    print("с:",list_c) 
   
