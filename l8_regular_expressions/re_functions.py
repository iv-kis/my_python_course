'''
Created on 13 авг. 2018 г.

@author: ivkis
'''
import re
pattern=r"spam"

#match
print('"re.match":')
if re.match(pattern,"eggspamsaugagespam"):
    print('  "spam" matches "eggspamsaugagespam"')
else:
    print('  "spam" doesn\'t match "eggspamsaugagespam"')

#search
print('"re.search":')    
if re.search(pattern,"eggspamsaugagespam"):
    print('  "spam" matches "eggspamsaugagespam"')
else:
    print('  "spam" doesn\'t match "eggspamsaugagespam"')
    
#findall
print('"re.findall":')    
print(" ",re.findall(pattern, "eggspamsaugagespam"))

#finditer: возвращает итератор из объектов типа match object // value:True, methods:start(),end(),group(),span()
print('"re.finditer":') 
for match in re.finditer(pattern, "eggspamsaugagespam"):
    print(" ","startpos:",match.start(),", match group:",match.group())    

#про методы match objects:
pattern=r"pam"
match=re.search(pattern,"eggspamsausage")
print("методы regex object (match object):")
print('  pattern=r"pam", string="eggspamsausage"')
if match:
    print("  match.group():",match.group())
    print("  match.start():",match.start())
    print("  match.end():",match.end())
    print("  match.span():",match.span())    

#подмена кусков строки с помощью .sub
string="My name is David, Hi David."
pattern=r"David"
newstr=re.sub(pattern,"Amy",string)
print('"newstring=re.sub("David","Amy",string)":\n ',"string: ",string)
print('  newstring: ',newstr)    
    
    