'''
Created on 11 авг. 2018 г.

@author: ivkis
'''
#############
'''
Изначально у нас был класс Celsius, поддерживающий обращение к .temperature
потом мы добавили upd, включающий set и get и проверку на абс. ноль
однако этот update не имеет обратной совместимости! 
надо рефакторить весь код, заменяя .temperature на set и get!
'''     
class Celsius:
    _min=-273.15
    def __init__(self, temperature = 0):
        self.set_temperature(temperature)
     
    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32
    
    def get_temperature(self):
        return self._temperature
    
    def set_temperature(self,value):
        if value<self._min:
            raise ValueError("Less than absolute zero!")
        self._temperature=value
        

a = Celsius(36.6)
print(a.get_temperature())
# get degrees Fahrenheit
print(a.to_fahrenheit())
print(a.__dict__)
#b=Celsius(-300)
c=Celsius()
#c.set_temperature(-300)

c._temperature=-300 
#Нарушаем правило, обращаясь к условно-private переменной! Так делать НЕ НАДО!
print(c.get_temperature())
