
import string
import random

print(" Only letters (1)\n Only digits (2)\n Only punctuations (3)\n Letters and digits (4)\n \
Letters and punctuations (5)\n Digits and punctuations (6)\n Letters, digits and punctuations (7)")

question = input("\nWhich characters do you want to create your password from? : ")

def fonk(value):
    password_len = int(input("How many characters should your password consist of? : "))
    x = ""
    for i in range(0,password_len):
        a = random.choice(value)
        x += a
    print(x)
    
if question == "1":
    value = string.ascii_letters
    fonk(value)
        
elif question == "2":
    value = string.digits
    fonk(value)

elif question == "3":
    value = string.punctuation
    fonk(value)

elif question == "4":
    value = string.ascii_letters + string.digits
    fonk(value)

elif question == "5":
    value = string.ascii_letters + string.punctuation
    fonk(value)


elif question == "6":
    value = string.punctuation + string.digits
    fonk(value)


elif question == "7":
    value = string.ascii_letters + string.digits + string.punctuation 
    fonk(value)

else:
    print("Please try again.")





