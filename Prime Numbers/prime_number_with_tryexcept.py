
def prime(n):
    if int(n) < 2:
        return -1
    
    elif n == 2:
        return 0
    elif int(n) > 2:
        for i in range(int(2),int(n)):
            if int(n) % i == 0:
                return -1
            elif i == int(n)-1:
                return 0
            
        
while True:
    try:
        n = input("Please enter a value: ")
        sonuc = prime(n)
        if sonuc == -1:
             print(f"The number {n} is not a prime number.")
        else:
            print(f"The number {n} is a prime number.")

    except ValueError:
        print("Please enter only a value.")
