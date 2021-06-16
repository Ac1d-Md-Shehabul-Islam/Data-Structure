class Data:
    
    def __init__(self,row,column):
        self.x = row
        self.y = column
        
    def elements(self):
        print("The data has", self.x,"rows and",self.y,"columns")
        
    def __add__(self,other):
        new_row = self.x + other.x
        new_column = self.y + other.y
        object_1 = Data(new_row,new_column)
        return object_1
        # return "New data has " + str(new_row) + " rows and " +            str(new_column) + " columns"  

#============================================================================


num1 = Data(10,20) 
num2 = Data(2,8)
num1.elements()
num2.elements()
num3 = num1 + num2
num3.elements()
# print(num1+num2)



