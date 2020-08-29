'''
Created on 13 авг. 2018 г.

@author: ivkis
'''
import re
if __name__=="__main__":
#(1) точка как произвольный символ
    pattern=r"gr.y"#rough string
    if re.match(pattern, "grey"): 
        print("gr.y matches grey")
    if re.match(pattern, "gray"): 
        print("gr.y matches gray")
    if not re.match(pattern, "blue"): 
        print("gr.y doesn't match blue")
    
#(2) ^ как начало строки, $ как конец
    pattern=r"^gr.y$"
    if re.match(pattern, "grey"): 
        print("^gr.y$ matches grey")
    if re.match(pattern, "gray"): 
        print("^gr.y$ matches gray")
    if not re.match(pattern, " gray"): 
        print("^gr.y$ doesn't match _gray")
    
#(3) character classes
    pattern=r"[aeiou]"
    if re.search(pattern, "grey"): 
        print("at least one of [aeiou] symbols is in 'grey'")
    if re.search(pattern, "qwertyuiop"): 
        print("at least one of [aeiou] symbols is in  'qwertyuiop'")
    if not re.search(pattern, "rythm myths"): 
        print("no [aeiou] in 'rythm myths'")

    pattern=r"[A-Z][A-Za-z][0-9]"
    if re.search(pattern, "LS3"): 
        print("pattern [A-Z][A-Za-z][0-9] accords 'LS3'")
    if re.search(pattern, "Ls3"): 
        print("pattern [A-Z][A-Za-z][0-9] accords 'Ls3'")
    if not re.search(pattern, "L3"): 
        print("pattern [A-Z][A-Za-z][0-9] doesn\'t accord 'Ls3'")
    if not re.search(pattern, "1ab"): 
        print("pattern [A-Z][A-Za-z][0-9] doesn\'t accord '1ab'")

    pattern=r"[^A-Z]"
    print('"re.search(r"[^A-Z],string)":')
    if re.search(pattern, "anvlkalvlll"): 
        print("  [^A-Z] inverts [A-Z] and is equal to [a-z]",", all in 'anvlkalvlll' are the lowercase")
    if re.search(pattern, "aABbCcDd"): 
        print("  there are some lowercase characters in 'aABbCcDd'")

#metacharacters *,+,?,{and} are specifying number of repetitions
    if re.match(r"egg(spam)*", "egg"): 
        print("egg(spam)* means >=0 repetitions of 'spam' after 'egg',True for 'egg'") 
    if re.match(r"egg(spam)+", "eggspamspamegg"): 
        print("egg(spam)+ means >=1 repetitions of 'spam' after 'egg', True for 'eggspamspamegg'") 
    if re.match(r"ice(-)?cream", "ice-cream"): 
        print("ice(-)?cream means 0 or 1 repetition of '-' between 'ice'and 'cream', True for both 'icecream' and 'ice-cream'")
    if re.match(r"ice(-){0,1}cream", "icecream"):
        print('The same is r"ice(-){0,1}cream"')