'''
Created on 16 авг. 2018 г.

@author: ivkis
'''
def method_revealing_decorator(method_to_decorate):
    def wrapper(self,*args,**kwargs):
        print("(на самом деле, ей {})".format(self.age))
        print(args)
        print(kwargs)
        return method_to_decorate(self,*args,**kwargs)
    return wrapper

class Lucy:
    def __init__(self):
        self.age=32
    @method_revealing_decorator
    def sayYourAge(self,lie=-3):
        print("Мне {}, а ты бы сколько дал?".format(self.age+lie))

lu=Lucy()
lu.sayYourAge(lie=-5)
        