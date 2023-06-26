# This is a guid to making an example of inheritance, Dog will inherit from this Pet
class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
# The super() function is used to call the constructor of the parent class. 
# This is a classic example of inheritance, which is a mechanism where a 
# new class is derived from an existing class.
class Dog(Pet):
    def __init__(self, name, age, breed):
        super().__init__(name, age,)
        self.breed = breed

my_dog = Dog("Shadow", 5,"German Shepard")
print (my_dog.name , my_dog.breed)