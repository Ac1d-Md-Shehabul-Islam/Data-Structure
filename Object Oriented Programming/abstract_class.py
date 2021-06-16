from abc import ABC, abstractmethod

class Animal(ABC):
    
    @abstractmethod         
    def sound(self):               #abstract method must not have any body
        pass
    
    def eat(self):
        print("The animal is eating")
        
#===========================================================================

class Dog(Animal):
    
    def sound(self):
        print("Dog is barking")
        
#===========================================================================

class Cat(Animal):
    
    def sound(self):
        print("Cat is meowing")
        
#===========================================================================

d1 = Dog()
d1.sound()
c1 = Cat()
c1.sound()
c1.eat()