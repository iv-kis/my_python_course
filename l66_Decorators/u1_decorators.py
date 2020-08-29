'''
Created on 16 авг. 2018 г.
Пример использования декоратора (коротко)
@author: ivkis
'''

def makebold(fn):
    def wrapped():
        return "<b>" + fn() + "</b>"
    return wrapped
 
def makeitalic(fn):
    def wrapped():
        return "<i>" + fn() + "</i>"
    return wrapped

@makebold
@makeitalic 
def hello():
    return "hello world"
 
if __name__ == '__main__':
    print(hello()) 
    # выведет <b><i>hello habr</i></b>