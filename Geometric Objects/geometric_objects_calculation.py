
def cube():
    value = int(input("Enter a side length: "))
    volume = value ** 3
    print(f"Volume of the cube: {volume}")


def rectangular_prism():
    value = int(input("Enter the first side length: "))
    value_2 = int(input("Enter the second side length: "))
    value_3 = int(input("Enter the third side length: "))
    volume = value * value_2 * value_3
    print(f"Volume of the Rectangular Prism: {volume}")


def right_pyramid():
    value = int(input("Enter the first side length: "))
    value_2 = int(input("Enter the second side length: "))
    height = int(input("Enter a height value: "))
    volume = (value * value_2 * height) / 3
    print(f"Volume of the Right Pyramid: {volume}")

import math

def cylinder():
    PI_number = math.pi
    radius = int(input("Enter a radius value: "))
    height = int(input("Enter a height value: "))
    volume = PI_number * (radius **2) * height
    print(f"Volume of the Cylinder: {volume}")


def right_cone():
    PI_number = math.pi
    radius = int(input("Enter a radius value: "))
    height = int(input("Enter a height value: "))
    volume = (PI_number * (radius **2) * height ) / 3
    print(f"Volume of the Right Cone: {volume}")    


def globe():
    PI_number = math.pi
    radius = int(input("Enter a radius value: "))
    volume = ( 4 * PI_number * (redius ** 3) )
    print(f"Volume of the Globe: {volume}")


def square():
    value = int(input("Enter a side length: "))
    perimeter = 4 * value
    area = value ** 2
    print(f"Perimeter of Square: {perimeter}")
    print(f"Area of Square: {area}")
    

def circle():
    PI_number = math.pi
    radius = int(input("Enter a radius value: "))
    perimeter = 2 * PI_number * radius
    print(f"Circumference of the Circle: {perimeter}")

    
def rectangle():
    value = int(input("Enter the first side length: "))
    value_2 = int(input("Enter the second side length: "))
    perimeter = (2 * value) + (2 * value_2)
    area = value * value_2
    print(f"Perimeter of Rectangle: {perimeter}")
    print(f"Area of Rectangle: {area}")


def parallelogram():
    value = int(input("Enter the first side length: "))
    value_2 = int(input("Enter the second side length: "))
    perimeter = (2 * value) + (2 * value_2)
    print(f"Perimeter of Parallelogram: {perimeter}")
    

def triangle():
    value = int(input("Enter the first side length: "))
    value_2 = int(input("Enter the second side length: "))
    value_3 = int(input("Enter the third side length: "))
    perimeter = value + value_2 + value_3    
    print(f"Perimeter of Tringle: {perimeter}")


def trapezoid():
    first_parallel_side = int(input("Enter the first parallel side length: "))
    second_parallel_side = int(input("Enter the second parallel side length: "))
    value = int(input("Enter the third side length: "))
    value_2 = int(input("Enter the last side length: "))
    height = int(input("Enter a height value: "))
    perimeter = first_parallel_side + second_parallel_side + value + value_2
    area = ((first_parallel_side + second_parallel_side) * height ) / 2
    print(f"Perimeter of Trapezoid: {perimeter}")
    print(f"Area of Trapezoid: {area}")
    
    
print(" Volume of the Cube (1)\n Volume of the Rectangular Prism (2)\n Volume of the Right Pyramid (3)\n Volume of the Cylinder \
(4)\n Volume of the Right Cone(5)\n Volume of the Globe (6)\n Perimeter and Area of ​​a Square (7)\n Circumference of the Circle (8)\n \
Perimeter and Area of ​​a Rectangle (9)\n Perimeter of ​​a Parallelogram (10)\n Perimeter of ​​a Triangle (11)\n Perimeter and Area of ​​a Trapezoid (12)")

while True:
    
    question = input("\nEnter the number of the action you want to make: ")

    if question == "1":
        cube()

    elif question == "2":
        rectangular_prism()

    elif question == "3":
        right_pyramid()

    elif question == "4":
        cylinder()

    elif question == "5":
        right_cone()

    elif question == "6":
        globe()

    elif question == "7":
        square()

    elif question == "8":
        circle()

    elif question == "9":
        rectangle()

    elif question == "10":
        parallelogram()

    elif question == "11":
        triangle()

    elif question == "11":
        triangle()
        
    elif question == "12":
        trapezoid()

    else:
        print("Error.Please try again.")


    
