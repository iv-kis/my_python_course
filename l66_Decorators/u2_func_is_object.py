'''
Created on 16 авг. 2018 г.

Функции в Python являются полноправными объектами:
ссылку на них можно передавать другой переменной, 
а ещё...

@author: ivkis
'''
def shout(word="да"):
    return word.upper()+"!"

if __name__ == '__main__':
     
    print('shout():',shout())
    # выведет: 'ДА!'
     
    # Так как функция - это объект, вы связать её с переменнной,
    # как и любой другой объект
    scream = shout
    print(' scream=shout')
 
    # Заметьте, что мы не используем скобок: мы НЕ вызываем функцию "shout",
    # мы связываем её с переменной "scream". Это означает, что теперь мы
    # можем вызывать "shout" через "scream":
     
    print('scream():',scream())
    # выведет: 'Да!'
    
    # Более того, это значит, что мы можем удалить "shout", и функция всё ещё
    # будет доступна через переменную "scream"
 
    del shout
    print(' shout is deleted.')
    
    try:
        print(shout())
    except NameError as e:
        print(e)
        #выведет: "name 'shout' is not defined"
     
    print('scream():',scream())
    # выведет: 'Да!'


