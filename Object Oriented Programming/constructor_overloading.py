# class Animal:
    
#     def __init__(self,*info):
#         if len(info) == 3:
#             self.name = info[0]
#             self.id = info[1]
#             self.action = info[2]
#         if len(info) == 2:
#             self.name = info[0]

            
#         if len(info) == 1:
#             self.name = info[0]
            
#         print('A Animal class object is created')    
#======================================================================

class Animal:
    
    def __init__(self,**info):
        if len(info) == 3:
            self.name = info['name']
            self.id = info['id']
            self.action = info['action']
        if len(info) == 2:
            self.name = info['name']
            self.id=info['id']

            
        if len(info) == 1:
            self.name = info['name']
            
        print('A Animal class object is created') 





p1 = Animal(name='Fox',id=54,action='sleeping')
p2 = Animal(name='Tiger',id=70)
p3 = Animal(name='Cat')
p4 = Animal()
