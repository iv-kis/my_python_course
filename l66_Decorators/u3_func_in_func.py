'''
Created on 16 авг. 2018 г.

Функции в Python являются полноправными объектами:
...их можно определять внутри другой функции.

@author: ivkis
'''
def talk():
    # Внутри определения функции "talk" мы можем определить другую...
    def whisper(word="да"):
        return word.lower()+"...";
 
    # ... и сразу же её использовать!
    print(whisper())

if __name__ == '__main__':
    # Теперь, КАЖДЫЙ РАЗ при вызове "talk", внутри неё определяется а затем
    # и вызывается функция "whisper".
    talk()
    # выведет: "да..."
     
    # Но вне функции "talk" НЕ существует никакой функции "whisper":
    try:
        print(whisper())
    except NameError as e:
        print(e)
        #выведет : "name 'whisper' is not defined"

