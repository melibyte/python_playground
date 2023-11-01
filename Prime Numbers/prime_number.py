

def prime(n):
    if n < 2:
        return -1
    elif n == 2:
        return 0
    elif n > 2:
        for i in range(2,n):
            if n % i == 0:
                return -1
            elif i == (n-1):
                return 0
            
        
while True:
    n = int(input("Please enter a value: "))
    sonuc = prime(n)
    
    if sonuc == -1:
        print(f"The number {n} is not a prime number.")
    else:
        print(f"The number {n} is a prime number.")




    
