
print(" Binary system to decimal system of numeration (1)\n \
Hexadecimal system to decimal system of numeration (2)\n Octo number system to decimal system of numeration (3)\n \
The result of a number in binary system (4)\n The result of a number octo number system (5)\n \
The result of a number in hexadecimal system (6)")

def b_to_d():
    question = input(" Which number do you want to convert?: ")
    result= int(question , 2)
    return result

def x_to_d():
    question = input(" Which number do you want to convert?: ")
    result= int(question , 16)
    return result

def o_to_d():
    question = input(" Which number do you want to convert?: ")
    result= int(question , 8)
    return result

def binary_system():
    question = int(input(" Which number do you want to convert?: "))
    return bin(question)[2:]

def octo_system():
    question = int(input(" Which number do you want to convert?: "))
    return oct(question)[2:]    

def hex_system():
    question = int(input(" Which number do you want to convert?: "))
    return hex(question)[2:]        

while True:

    action= input(" Which action do you want to take?: ")

    if action == "1":
        print(b_to_d())

    elif action == "2":
        print(x_to_d())

    elif action == "3":
        print(o_to_d())

    elif action == "4":
        print(binary_system())

    elif action == "5":
        print(octo_system()) 

    elif action == "6":
        print(hex_system()) 

