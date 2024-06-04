# Animal is the base class.
class Animal(object):
    pass
# class dog inherits the value of animal class.
class Dog(Animal):
# A class representing dogs with an attribute 'name'.   
    def __init__(self,name):
        self.name = name

class Cat(Animal):
    def __init__(self,name):
        self.name = name
# A class representing people. Has an attribute name and can have a pet.
class Person(object):
    def __init__(self,name):
        self.name = name
        self.pet = None
# Inherited from person. Have an additional attribute 'salary'.
class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary
# A base class for all kind of fish.
class Fish(object):
    pass
# class that inherited from Fish.
class Salmon(Fish):
    pass

class Halibut(Fish):
    pass
# An instance of Dog is created with rover
rover = Dog("Rover")

satan = Cat("Satan")
# AN instance of person is created with the name 'Mary'
mary = Person("Mary")

mary.pet = satan

frank = Employee("Frank", 120000)

frank.pet = rover
#  Empty instances.
flipper = Fish()

crouse = Salmon()

harry = Halibut()