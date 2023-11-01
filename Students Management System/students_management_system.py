
students = { "Name1 Surname1" : {"Age" :20
                                 "Department":"Computer Engineering"
                                 "Grade": "1st Grade" }
    
             "Name2 Surname2" : {"Age": 20
                              "Department": "Computer Engineering"
                              "Grade": "2nd Grade"}


def add_student():
    name = input("What is the student's name and surname?: ")
    age = int(input("How old is student?: "))
    department = input("What is the student's department?: ")
    grade = input("What grade is the student?")

    value = {"Age": age
             "Department": department
             "Grade": grade}

    students[name]= value
    return students


def del_student():
    
    name =input("Type the name of the student you want to delete: ")
    value = students.pop(name)
    return students

def update_student():
    pass



print(" Add Student (1)\n Delete student (2) ")

while True:
    
    question = input("\nSelect the action you want to do: ")

    if question == "1":
        print(add_student())

    elif question == "2":
        print(del_student())
    
