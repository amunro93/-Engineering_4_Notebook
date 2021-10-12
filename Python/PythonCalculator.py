a = int(input("Enter first number: "))
b = int(input("Enter second number: "))



def doMath(a,b,c): 
    if c == 1:  #Defines Sum
        
        return str (a + b)
        
    if c == 2:  #Defines Difference
        
        return str (a - b)
    
    if c == 3:  #Defines Product
        
        return str (a * b)
    
    if c == 4:  #Defines Quotient 
        
        return str (a / b)
        
    if c == 5:  #Defines Modulo
        
        return str (a % b)
        
        
        
print("Sum:\t\t" + doMath(a,b,1))
print("Difference:\t" + doMath(a,b,2))
print("Product:\t" + doMath(a,b,3))
print("Quotient:\t" + doMath(a,b,4))
print("Modulo:\t\t" + doMath(a,b,5))
