'''
@classmethod модифицирует конструктор класса, позволяя создавать объекты
с помощью синтаксиса new_object=ClassName.ClassMethod(). Т.е. вызывается 
конструктор с дополнительными опциями.

classmethod принимает и возвращает обязательный параметр cls
'''
class Rectangle:
    def __init__(self,a,b):
        self.side_a=a
        self.side_b=b    
    def calculateArea(self):
        self.area=self.side_a*self.side_b
        return self.area 
    @classmethod
    def square(cls,side):
        return cls(side,side)
    @staticmethod
    def checkSides(a,b):
        if a<=0 or b<=0:
            raise ValueError("Sides aren't positive")
        else:
            return True
a_side=int(input('side 1'))
b_side=int(input('side 2'))

if Rectangle.checkSides(a_side, b_side):
    rect=Rectangle(a_side,b_side)
print(rect.calculateArea())
sq=Rectangle.square(2)
print(sq.calculateArea())