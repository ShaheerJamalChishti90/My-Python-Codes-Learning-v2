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

def change_student_info():
    student_roll = int(input("Enter the student Roll No: "))
    for i in all_students:
        if i['Roll#'] == student_roll:
            print("1-Name\n2-Roll#\n3-Age\n4-Marks")
            user_choice = int(input("Enter your choice here: "))
            if user_choice == 1:
                name = input("Enter the name here: ")
                i["Name"] = name 
            elif user_choice == 2:
                roll = int(input("Enter the roll here: "))
                i["Roll#"] = roll 
            elif user_choice == 3:
                age = int(input("Enter the age here: "))
                i["Age"] = age 
            elif user_choice == 4:
                marks = int(input("Enter the marks here: "))
                i["Marks"] = marks 
            else:
                print("Invalid Entry")
                break
                
def delete_student():
    student_roll = int(input("Enter the student Roll No you wanna delete: "))
    for i in all_students:
        if student_roll == i["Roll#"]:
            all_students.remove(i)
        else:
            print("Invalid Entry!")

def load_data_into_file():
    with open("./Project/Students_Record.txt", "a") as f:
        for i in all_students:
            f.write(str(i))
        print("Data has been loaded successfully into a file!")

def read_data():
    with open("./Project/Students_Record.txt", "r") as f:
        print(f.read())
        
def average_marks_grades():
    for i in all_students:
        if i["Marks"] > 50:
            print(f"{i["Name"]}: Pass")
        else:
            print(f"{i["Name"]}: Fail")
            

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
        
    elif user_choice == 5:
        change_student_info()

    elif user_choice == 6:
        delete_student()
        
    elif user_choice == 7:
        load_data_into_file()
        
    elif user_choice == 8:
        read_data()
        
    elif user_choice == 9:
        average_marks_grades()
        
    else:
        print("This option is not available yet.\n")
        
            