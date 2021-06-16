class Vehicle:
    
    def __init__(self,type,model,year):
        self.type = type
        self.model = model
        self.year = year
        print(self)
        
    
    def __str__(self):
        return "Vehice Type: " + self.type + "\nModel: "+ self.model+"\nRegistration Year: " + str(self.year)

#===========================================================================

a = Vehicle('Car','Axio',2003)
# print(a.__str__())