class FractionData:
    def __init__(self,n,d):
        self.num = n
        self.den = d
    
    def __str__(self):
        return f"{self.num}/{self.den}"
    
    def __add__(self,other):
        temp_num = self.num*other.den + other.num*self.den
        temp_den = self.den*other.den
        return f"{temp_num}/{temp_den}"
    
    def __sub__(self,other):
        temp_num = self.num*other.den - other.num*self.den
        temp_den = self.den*other.den
        return f"{temp_num}/{temp_den}"
   
    def __mul__(self,other):
        temp_num = self.num*other.num 
        temp_den = self.den*other.den
        return f"{temp_num}/{temp_den}"
    
    def __truediv__(self,other):
        temp_num = self.num*other.den
        temp_den = self.den*other.num
        return f"{temp_num}/{temp_den}"
    
a = FractionData(3,7)
b = FractionData(4,9)
print(a)
print(b)
print(a+b)
print(a-b)
print(a*b)
print(a / b)