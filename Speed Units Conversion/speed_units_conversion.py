print("\n1. m/s to m/h \n2. m/h to m/s \n3. m/s to m/min \n4. m/min to m/s \n5. m/s to km/h \n6. km/h to m/s \n7. m/s to km/min \n8. km/min to m/s \
       \n9. m/s to km/s \n10. km/s to m/s \n11. m/s to cm/h \n12. cm/h to m/s \n13. m/s to cm/min \n14. cm/min to m/s \n15. m/s to cm/s \n16. cm/s to m/s \
       \n17. m/s to mm/h \n18. mm/h to m/s \n19. m/s to mm/min \n20. mm/min to m/s \n21. m/s to mm/s \n22. mm/s to m/s\n")

while True:

    question = input("What action do you want to do? Enter the number: ")

    if question == "1":
        n = float(input("Enter a value: "))
        result = 3600 * n
        print (f"{n} m/s = {result} m/h")

    elif question == "2":
        n = float(input("Enter a value: "))
        result = 0.000277777777777778 * n
        print (f"{n} m/h = {result} m/s")

    elif question == "3":
        n = float(input("Enter a value: "))
        result = 60 * n
        print (f"{n} m/s = {result} m/min")

    elif question == "4":
        n = float(input("Enter a value: "))
        result = 0.0166666666666667 * n
        print (f"{n} m/min = {result} m/s")

    elif question == "5":
        n = float(input("Enter a value: "))
        result = 3.6 * n
        print (f"{n} m/s = {result} km/h")

    elif question == "6":
        n = float(input("Enter a value: "))
        result = 0.277777777777778 * n
        print (f"{n} km/h = {result} m/s")

    elif question == "7":
        n = float(input("Enter a value: "))
        result = 0.06 * n
        print (f"{n} m/s = {result} km/min")

    elif question == "8":
        n = float(input("Enter a value: "))
        result = 16.6666666666667 * n
        print (f"{n} km/min = {result} m/s")

    elif question == "9":
        n = float(input("Enter a value: "))
        result = 0.001 * n
        print (f"{n} km/min = {result} km/s")

    elif question == "10":
        n = float(input("Enter a value: "))
        result = 1000 * n
        print (f"{n} km/s = {result} m/s")        

    elif question == "11":
        n = float(input("Enter a value: "))
        result = 360000 * n
        print (f"{n} m/s = {result} cm/h")

    elif question == "12":
        n = float(input("Enter a value: "))
        result = 0.00000277777777777778 * n
        print (f"{n} cm/h = {result} m/s")

    elif question == "13":
        n = float(input("Enter a value: "))
        result = 6000 * n
        print (f"{n} m/s = {result} cm/min")

    elif question == "14":
        n = float(input("Enter a value: "))
        result = 0.000166666666666667 * n
        print (f"{n} cm/min = {result} m/s")

    elif question == "15":
        n = float(input("Enter a value: "))
        result = 100 * n
        print (f"{n} m/s = {result} cm/s")

    elif question == "16":
        n = float(input("Enter a value: "))
        result = 0.01 * n
        print (f"{n} cm/s = {result} m/s")

    elif question == "17":
        n = float(input("Enter a value: "))
        result = 3600000 * n
        print (f"{n} m/s = {result} mm/h")

    elif question == "18":
        n = float(input("Enter a value: "))
        result = 0.000000277777777777778 * n
        print (f"{n} mm/h = {result} m/s")

    elif question == "19":
        n = float(input("Enter a value: "))
        result = 60000 * n
        print (f"{n} m/s = {result} mm/min")

    elif question == "20":
        n = float(input("Enter a value: "))
        result = 0.0000166666666666667 * n
        print (f"{n} mm/min = {result} m/s")

    elif question == "21":
        n = float(input("Enter a value: "))
        result = 1000 * n
        print (f"{n} m/s = {result} mm/s")

    elif question == "22":
        n = float(input("Enter a value: "))
        result = 0.001 * n
        print (f"{n} mm/s = {result} m/s")





        
