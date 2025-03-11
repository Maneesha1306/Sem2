from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle:
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
    def perimeter(self):
        return 2*(self.width+self.height)
    
w=int(input())
h=int(input())
rect=Rectangle(w,h)
print(rect.area())
print(rect.perimeter())

s=Shape()