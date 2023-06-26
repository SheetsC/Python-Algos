# Polymorphism refers to the ability of an object to take on many forms. 
# In OOP, polymorphism allows a subclass to have a specific implementation 
# of a method that is already defined in its superclass. This can be achieved 
# through method overriding.

class Animal:
    def speak(self):
        return "Some sound"

class Dog(Animal):
    def speak(self):
        return "Woof"

class Cat(Animal):
    def speak(self):
        return "Meow"

animals = [Dog(), Cat()]
# When we iterate through a list of animals and call their speak method, 
# the version that matches their actual object type is called. 
for animal in animals:
    print(animal.speak())
