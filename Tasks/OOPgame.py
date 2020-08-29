'''
Created on 11 авг. 2018 г.

@author: ivkis
'''
class GameObject: 
    class_name = "" 
    desc = "" 
    objects = {} 
 
    def __init__(self, name): 
        self.name = name 
        GameObject.objects[self.class_name] = self #словарь существующих объектов данного класса: {Goblin:}
 
    def get_description(self): 
        return self.class_name + "\n" + self.desc 
 
class Goblin(GameObject): 
    class_name = "goblin" 
    desc = "A foul creature" 
 
goblin = Goblin("Gobbly") 
 
def get_input():
    command = input(": ").split() 
    verb_word = command[0] 
    print(verb_word)
    if verb_word in verb_dict: 
        verb = verb_dict[verb_word] #назначается функция для соответствующей команды
    else: 
        print("Unknown verb {}". format(verb_word)) 
        return 
    if len(command) >= 2: 
        noun_word = command[1] 
        print (verb(noun_word)) 
    else: 
        print(verb("nothing")) 
   
#обработчики команд say и examine
def say(noun): 
    return 'You said "{}"'.format(noun) 

def examine(noun): 
    if noun in GameObject.objects: 
        return GameObject.objects[noun].get_description() 
    else: 
        return "There is no {} here.".format(noun)
    

#в этом словаре задаётся, что делать при поступлении команды
verb_dict = {
    "say":say, 
    "examine":examine
} 
 
while True: 
    get_input()