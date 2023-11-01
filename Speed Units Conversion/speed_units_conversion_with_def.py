
print("1. m/s to m/h \n2. m/h to m/s \n3. m/s to m/min \n4. m/min to m/s \n5. m/s to km/h \n6. km/h to m/s \n7. m/s to km/min \n8. km/min to m/s \
       \n9. m/s to km/s \n10. km/s to m/s \n11. m/s to cm/h \n12. cm/h to m/s \n13. m/s to cm/min \n14. cm/min to m/s \n15. m/s to cm/s \n16. cm/s to m/s \
       \n17. m/s to mm/h \n18. mm/h to m/s \n19. m/s to mm/min \n20. mm/min to m/s \n21. m/s to mm/s \n22. mm/s to m/s\n")

def ms_to_mh(n):
    result_1 = 3600 * n
    return result_1

def conversion_2(n):
    result_2 = 0.000277777777777778 * n
    return result_2

def conversion_3(n):
    result_3 = 60 * n
    return result_3

def conversion_4(n):
    result_4 = 0.0166666666666667 * n
    return result_4

def conversion_5(n):
    result_5 = 3.6 * n
    return result_5

def conversion_6(n):
    result_6 = 0.277777777777778 * n
    return result_6

def conversion_7(n):
    result_7 = 0.06 * n
    return result_7

def conversion_8(n):
    result_8 = 16.6666666666667 * n
    return result_8

def conversion_9(n):
    result_9 = 0.001 * n
    return result_9

def conversion_10(n):
    result_10 = 1000 * n
    return result_10

def conversion_11(n):
    result_11 = 360000 * n
    return result_11

def conversion_12(n):
    result_12 = 0.00000277777777777778 * n
    return result_12

def conversion_13(n):
    result_13 = 6000 * n
    return result_13

def conversion_14(n):
    result_14 = 0.000166666666666667 * n
    return result_14

def conversion_15(n):
    result_15 = 100 * n
    return result_15

def conversion_16(n):
    result_16 = 0.01 * n
    return result_16

def conversion_17(n):
    result_17 = 3600000 * n
    return result_17

def conversion_18(n):
    result_18 = 0.000000277777777777778 * n
    return result_18

def conversion_19(n):
    result_19 = 60000 * n
    return result_19

def conversion_20(n):
    result_20 = 0.0000166666666666667 * n
    return result_20

def conversion_21(n):
    result_21 = 1000 * n
    return result_21

def conversion_22(n):
    result_22 = 0.001 * n
    return result_22



while True:

    question = input("What action do you want to do? Enter the number: ")

    if question == "1":
        n = float(input("Enter a value: "))
        print (f"{n} m/s = {ms_to_mh(n)} m/h")

    elif question == "2":
        n = float(input("Enter a value: "))
        print (f"{n} m/h = {conversion_2(n)} m/s")

    elif question == "3":
        n = float(input("Enter a value: "))
        print (f"{n} m/s = {conversion_3(n)} m/min")

    elif question == "4":
        n = float(input("Enter a value: "))
        print (f"{n} m/min = {conversion_4(n)} m/s")

    elif question == "5":
        n = float(input("Enter a value: "))
        print (f"{n} m/s = {conversion_5(n)} km/h")

    elif question == "6":
        n = float(input("Enter a value: "))
        print (f"{n} km/h = {conversion_6(n)} m/s")

    elif question == "7":
        n = float(input("Enter a value: "))
        print (f"{n} m/s = {conversion_7(n)} km/min")

    elif question == "8":
        n = float(input("Enter a value: "))
        print (f"{n} km/min = {conversion_8(n)} m/s")

    elif question == "9":
        n = float(input("Enter a value: "))
        print (f"{n} km/min = {conversion_9(n)} km/s")

    elif question == "10":
        n = float(input("Enter a value: "))
        print (f"{n} km/s = {conversion_10(n)} m/s")        

    elif question == "11":
        n = float(input("Enter a value: "))
        print (f"{n} m/s = {conversion_11(n)} cm/h")

    elif question == "12":
        n = float(input("Enter a value: "))
        print (f"{n} cm/h = {conversion_12(n)} m/s")

    elif question == "13":
        n = float(input("Enter a value: "))
        print (f"{n} m/s = {conversion_13(n)} cm/min")

    elif question == "14":
        n = float(input("Enter a value: "))
        print (f"{n} cm/min = {conversion_14(n)} m/s")

    elif question == "15":
        n = float(input("Enter a value: "))
        print (f"{n} m/s = {conversion_15(n)} cm/s")

    elif question == "16":
        n = float(input("Enter a value: "))
        print (f"{n} cm/s = {conversion_16(n)} m/s")

    elif question == "17":
        n = float(input("Enter a value: "))
        print (f"{n} m/s = {conversion_17(n)} mm/h")

    elif question == "18":
        n = float(input("Enter a value: "))
        print (f"{n} mm/h = {conversion_18(n)} m/s")

    elif question == "19":
        n = float(input("Enter a value: "))
        print (f"{n} m/s = {conversion_19(n)} mm/min")

    elif question == "20":
        n = float(input("Enter a value: "))
        print (f"{n} mm/min = {conversion_20(n)} m/s")

    elif question == "21":
        n = float(input("Enter a value: "))
        print (f"{n} m/s = {conversion_21(n)} mm/s")

    elif question == "22":
        n = float(input("Enter a value: "))
        print (f"{n} mm/s = {conversion_22(n)} m/s")








        
