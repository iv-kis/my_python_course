'''
Created on 16 авг. 2018 г.

@author: ivkis
'''
def my_decorator1(func):
    def decorated():
        print("Action before")
        func()
        print("Action after")
    return decorated

def doubledashes(func):
    def decorated():
        print("========")
        func()
        print("========")
    return decorated

def my_func_1():
    print("Hello world 1")


@my_decorator1
@doubledashes
def my_func_2():
    print("Hello world 2")

if __name__ == '__main__':
    my_decorator1(my_func_1)()
    print()
    my_func_2()
    