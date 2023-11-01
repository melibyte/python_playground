
print(" 1. Celsius to fahrenheit\n 2. Fahrenheit to Celsius\n 3. Celsius to kelvin\n 4. Kelvin to celsius\n 5. Fahrenheit to Kelvin\n 6. Kelvin to Fahrenheit")

def celsius_to_fahrenheit(celsius):
    result_1 = ((celsius * 1.8) +32)
    return result_1

def fahrenheit_to_celsius(fahrenheit):
    result_2 = ((fahrenheit -32) / 1.8)
    return result_2

def celsius_to_kelvin(celsius):
    result_3 = celsius +273
    return result_3

def kelvin_to_celsius(kelvin):
    result_4 = kelvin -273
    return result_4

def fahrenheit_to_kelvin(fahrenheit):
    result_5 = (((fahrenheit +459.67) *5) /9)
    return result_5

def kelvin_to_fahrenheit(kelvin):
    result_6 = ( ((kelvin*9) /5) -459.67)
    return result_6

while True:

    question = input("What action do you want to do? Enter the number: ")
        
    if question == "1":
        celsius = float(input("Enter a value: "))
        print(f"{celsius}°C = {celsius_to_fahrenheit(celsius)}°F ")
            
    elif question == "2":
        fahrenheit = float(input("Enter a value: "))
        print(f"{fahrenheit}°F = {fahrenheit_to_celsius(fahrenheit)}°C  ")

    elif question == "3":
        celsius = float(input("Enter a value: "))
        print(f"{celsius}°C = {celsius_to_kelvin(celsius)} K ")

    elif question == "4":
        kelvin = float(input("Enter a value: "))
        print(f"{kelvin} K = {kelvin_to_celsius(kelvin)}°C  ")

    elif question == "5":
        fahrenheit = float(input("Enter a value: "))
        print(f"{fahrenheit}°F = {fahrenheit_to_kelvin(fahrenheit)} K  ")

    elif question == "6":
        kelvin = float(input("Enter a value: "))
        print(f"{kelvin} K = {kelvin_to_fahrenheit(kelvin)}°F ")

    else:
        print("Please try again.")

    



