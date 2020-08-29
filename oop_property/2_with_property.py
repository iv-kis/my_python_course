'''
Created on 20 авг. 2018 г.

@author: ivkis
'''
class Celsius:
    def __init__(self, temperature=0):
        self.temperature=temperature
        
    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32
    
    def set_temperature(self, value):
        if value < -273:
            raise ValueError("Temperature below -273 is not possible!")
        print("Setting value")
        self._temperature = value
    
    def get_temperature(self):
        print("Getting value")
        return self._temperature 
    
    temperature=property(get_temperature,set_temperature)
    
c=Celsius(35)
print(c.temperature)
c.temperature=38
print(c.temperature)
print(c.__dict__)
#c.temperature=-300