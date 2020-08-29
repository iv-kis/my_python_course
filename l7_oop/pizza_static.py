'''
Created on 20 авг. 2018 г.

@author: ivkis
'''
class Pizza: 
    def __init__(self, toppings): 
        self.toppings = toppings 

    @staticmethod 
    def validate_topping(topping): 
        if topping == "pineapple": 
            raise ValueError("No pineapples!") 
        else: 
            return True 

ingredients = ["cheese", "onions", "spam"] 
if all(Pizza.validate_topping(i) for i in ingredients): 
    pizza = Pizza(ingredients)
    print(pizza.toppings)