print("Enter:\n1-Add a new Student;\n2-Display the student info;\n3-Seach the student by RolL#;\n4-Sort Students by marks;\n5-Update the stuent's info;\n6-Delete a Student;\n7-Save all data to a File'\n8-Load student data from a file;\n9-Show average marks and grade calculation;\n10-Exit")

all_students = []

def add_student():
    st_name = input("Enter your name here: ") 
    st_roll = int(input("Enter your roll no here: "))
    st_age = int(input("Enter your age here: "))
    st_marks = int(input("Enter your marks here: "))

    student = {
        "Name": st_name, 
        "Roll#": st_roll,
        "Age":st_age,
        "Marks":st_marks
    }
    
    all_students.append(student)
    print("Added Successfully")
    


def show_students():
    print(all_students) 
    
def search_student():
    student_roll = int(input("Enter the student Roll No: "))
    for i in all_students:
        if i['Roll#'] == student_roll:
            print(f"Student Name: {i["Name"]}\nStudent Roll#: {i["Roll#"]}\nStudent Age: {i["Age"]}\nStudent Marks: {i["Marks"]}")
        
def sort_students():
    sorted_marks = []
    for i in all_students:
        sorted_marks.append(i['Marks'])
    print(f"Here are the sorted marks of all Students: {sorted(sorted_marks)}")



while True:
    try:
        user_choice = int(input("Enter your choice here: "))

    except ValueError:
        print("Invalid input! Please enter a number from 1 to 10.\n")
        continue

    if user_choice == 10:
        print("Thanks for using our SMS!")
        break
    elif user_choice == 1:
        add_student()

    elif user_choice == 2:
        show_students() 
        
    elif user_choice == 3:
        search_student()
        
    elif user_choice == 4:
        sort_students()
    else:
        print("This option is not available yet.\n")
        
            