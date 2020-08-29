'''
Created on 13 авг. 2018 г.

@author: ivkis
'''
import re
if __name__ == '__main__':
    pattern=r"([\w\.-\\']+)@([\w\.-\\']+)(\.[\w\.]+)"
    str1="Please contact email'1@domain.com for assistance" 
    str2="Please contact email'1@domain.com or email'2@domain.com"
    match=re.search(pattern,str1)
    if match:
        print(match.group())
    match=re.findall(pattern,str2)
    if match:
        for matches in match:   
            print(matches[0]+"@"+matches[1]+matches[2])