class Calculator: 
    def calculate(self,a,b=0,c=0 ): 
        for i in (a,b,c): 
            if type(i) not in (int,float): 
                raise ValueError("it must be in integer and float") 
        if a!=0 and b!=0 and c!=0 : 
            return a*b*c
        elif a!=0 and b!=0 and c==0: 
            return a+b 
        elif a!=0 and b==0 and c==0: 
            return a**2
c=Calculator() 
print(c.calculate(2))           
print(c.calculate(2, 3))        
print(c.calculate(2, 3, 4))     
print(c.calculate(2,3,"4"))  