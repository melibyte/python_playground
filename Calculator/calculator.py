
print("Summation (1) \nSubstract (2) \nMultiply (3) \nDivision (4) \nAbsolute Value (5) \nCalculate the percentage (6) \nCalculate the Factorial (7) \
       \nCalculate the Exponent (8) \nTake the square root (9) \nCovert from radian to degree (10) \nConvert from degree to radian (11) \nCalculate logarithms (12) \
       \nCalculate logarithms in base e (13) \nCalculate e**x(e to the x) (14) \nCalculate sine (15) \nCalculate cosine (16) \nCalculate tangent (17) \
       \nCalculate the greatest common factor (18) \nCalculate the least common multiple (19)")

def calc_sum():
    result = 0
    a = input("How many numbers do you want to sum?: ")
    for i in range(1,int(a)+int(1)):
        number=float(input(f"{i}. Number : "))
        result= result + number
    return result

def calc_subst():
    a = float(input("Enter a value: "))
    b = float(input("Enter the second value: "))
    return a-b

def calc_mult():
    result = 1
    a = input("How many numbers do you want to multiply?: ")
    for i in range(1,int(a)+int(1)):
        number=float(input(f"{i}. Number : "))
        result= result * number
    return result

def calc_division():
    a = float(input("Enter a value: "))
    b = float(input("Enter the second value: "))
    return a*b

def calc_per():
    a = int(input("Enter a value: "))
    b = int(input("What percentage of the number you entered do you want to calculate?: "))
    result = ((a*b) /100)
    return result

def calc_fact(n):
    if n.isdigit() == False:
        return -1
    n = int(n)
    
    number = 1
    for  i in range(1,n+1):     
        number *= i
    return number

import math

def calc_pow():
    a = int(input("Enter a value: "))
    b = int(input("Enter the second value: "))  
    result = math.pow(a,b)
    return result

def calc_sqrt():
    n = int(input("Enter a value: "))
    result=math.sqrt(n)
    return result

def radian_to_degree():
    n = float(input("Enter a value: "))
    result = math.degrees(n)
    return result

def degree_to_radian():
    n = float(input("Enter a value: "))
    result =math.radians(n)
    return result

def calc_log():
    a = int(input("Enter a value: "))
    b = int(input("Enter second value: "))
    result = math.log(a,b)
    return result

def calc_loge():
    n = int(input("Enter a value: "))
    result = math.log1p(n)
    return result

def calc_exp():
    n = float(input("Enter a value: "))
    result = math.exp(n)
    return result

def calc_sin():
    n = float(input("Enter a value: "))
    result = math.sin(math.radians(n))
    return result

def calc_cos():
    n = float(input("Enter a value: "))
    result = math.cos(math.radians(n))
    return result

def calc_tan():
    n = float(input("enter a value: "))
    result =math.tan(math.radians(n))
    return result

def calc_gcd():
    a = int(input("Enter a value: "))
    b = int(input("Enter second value: "))
    result = math.gcd(a,b)
    return result

def calc_ekok():
    a = int(input("Enter a value: "))
    b = int(input("Enter second value: "))
    result = (a*b)/ math.gcd(a,b)
    return result

while True:
    
    question = input("What action do you want to do? Enter the number: ")

    if question == "1":
        print("Sum of entered numbers: ", calc_sum())
        
    elif question == "2":
        print(calc_subst())

    elif question == "3":
        print("Multiply of entered numbers: ",calc_mult())

    elif question == "4":
        print(calc_division())
        
    elif question == "5":
        n = float(input("Enter a value: "))
        print(abs(n))

    elif question == "6":
        print(calc_per())

    elif question == "7":
        n = input("Enter a value: " )
        result = calc_fact(n)
        
        if result == -1:
            print("Please enter a value.")   
      
        else:
            print(f"{n}! =", result)
        
    elif question == "8":
        print(calc_pow())

    elif question =="9":
        print(calc_sqrt())

    elif question =="10":
        print(radian_to_degree())

    elif question =="11":
        print(degree_to_radian())

    elif question =="12":
        print(calc_log())

    elif question =="13":
        print(calc_loge())

    elif question =="14":
        print(calc_exp())

    elif question =="15":
        print(calc_sin())

    elif question =="16":
        print(calc_cos())

    elif question =="17":
        print(calc_tan())

    elif question =="18":
        print(calc_gcd())

    elif question =="19":
        print(calc_ekok())

    else:
        print("Please try again.")





