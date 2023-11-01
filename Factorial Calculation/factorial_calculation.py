   

def factorial(n):
    if n.isdigit() == False:
        return -1
    n = int(n)
    
    number = 1
    for  i in range(1,n):     
        number *= i
    return number



while True:
    n = input("Please enter a value: " )
    result = factorial(n)
    
    if result == -1:
        print("Please enter a value.")   
        
  
    else:
        print(f"{n}! =", result)
    







        
    








        
            
    
