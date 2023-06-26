# Abstraction is used for classes and methods that are not instantiated
# rather they used as rules for instantiation of subclasses. abstract methods 
# are intended to be overridden when making the subclassed and thier methods. 
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    @abstractmethod
    def perimeter(self):
        pass
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    def perimeter(self):
        return 3.14 * 2 * self.radius
