class Student:
    
    def __init__(self,name,id):
        self.name = name
        self.__id = id
        
    def details(self):
        print("Name:",self.name,"\nID:",self.__id)
#===========================================================================  
class CSEStudent(Student):
 
    def __init__(self,name,id,no_of_lab):
        super().__init__(name,id)
        self.labs = no_of_lab      
        
    def cry(self):
        print("CSE students have",self.labs,"labs each semester")
#===========================================================================
class BBAStudent(Student):
    
    def party(self):
        print("BBA Students chill because they have no labs")            
#===========================================================================

c1 = CSEStudent('Siam',20,3)
c2 = BBAStudent('Nayeem',39)
c1.details()
print("\n")
c2.details()
c1.cry()

