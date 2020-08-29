'''
Created on 16 авг. 2018 г.

@author: ivkis
'''
def doSomethingBefore(func):
    print("Я делаю что-то, перед тем как вызвать функцию, которую ты мне передал")
    print(func())
    
def getTalk(type="shout"):
    # Мы определяем функции прямо здесь
    def shout(word="да"):
        return word.upper()+"!"
 
    def whisper(word="да") :
        return word.lower()+"...";
    
    # Затем возвращаем необходимую
    if type == "shout":
        # Заметьте, что мы НЕ используем "()", нам нужно не вызвать функцию,
        # а вернуть объект функции
        return shout
    else:
        return whisper
 
if __name__ == '__main__':
    # Как использовать это непонятное нечто?
    # Возьмём функцию и свяжем её с переменной
    talk = getTalk() #getTalk() возвращает "shout"(объект-функцию)
     
    # Как мы можем видеть, "talk" теперь - объект "function":
    print("print(talk):",talk)
    # выведет: <function shout at 0xb7ea817c>
     
    # Который можно вызывать, как и функцию, определённую "обычным образом":
    print("print(talk()):",talk())
     
    # Если нам захочется - можно вызвать её напрямую из возвращаемого значения:
    print("print(talk('whisper')):",getTalk("whisper")())
    # выведет: да...
    
    doSomethingBefore(talk)
    #выведет:
    # Я делаю что-то ещё, перед тем как вызвать функцию, которую ты мне передал
    # Да!