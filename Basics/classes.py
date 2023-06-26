# This is the basic creation and displaying of the Class and attribute concepts.


class Car:
    def __init__(self, color, speed):
        self.color = color
        self.speed = speed
# we are creating an instace method that utilizes encapulation "self.color"
    def show_info(self):
        print(f'car is {self.color} and goes {self.speed}')
car= Car("red", "100mph")
car.show_info()