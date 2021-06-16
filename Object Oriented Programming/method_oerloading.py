from multipledispatch import dispatch

class Calculator:
    
    @dispatch(int,int)
    def product(self,a,b):
        print(a*b)
        
    @dispatch(int,int,int)
    def product(self,a,b,c):
        print(a*b*c)
        
        
    @dispatch(float,float)
    def product(self,a,b):
        print(a*b)
        
    @dispatch(str, int)
    def product(self,a,b):
        print(int(a)*b)

#========================================================================


a = Calculator()
a.product(3.0,4.5)
  