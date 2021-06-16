class Student:
    
    def __init__(self, name, id):
        self.name = name        #public variable
        self.__id = id          #private variable
        
    def details(self):
        print("Student name:", self.name, "ID:",self.__id)
    
    
    def update_id(self,ID):
        if ID>0:
            self.__id = ID
        else:
            print("Invalid ID, Enter a New ID")
    
#============================================================================


a = Student('Siam',50)
b = Student('Jack',40)

a.__id = 50 # no use

a.update_id(40)
a.details()
b.details()

