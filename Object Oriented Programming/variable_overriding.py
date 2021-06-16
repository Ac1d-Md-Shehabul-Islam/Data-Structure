class Animal:
    
    def __init__(self,name):
        self.name = name
        self.color = "White"
        
    def eat(self):
        print(self.color,self.name,"is eating")
#===========================================================================           
class Dog(Animal):
    
    def __init__(self,name,color):
        super().__init__(name)
        self.color = color
        
    def bark(self):
        print(self.color,self.name,"is barking")
#===========================================================================

d1 = Dog('Jhonson','Black')
d1.bark()
d1.eat()