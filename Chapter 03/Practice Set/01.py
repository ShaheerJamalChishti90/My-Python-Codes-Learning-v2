# Q1: Write a python program to display a user entered name followed by Good Afternoon using input () function

name = input("Enter your name here: ")
gender = input("Enter your gender here: ")

gender_real = gender

match gender_real:
    
    case "male":
        print(f'Good Afternoon Mr. {name}')
    case "female":
        print(f"Good Afternoon Ms. {name}")
    case _ if gender_real == "transgender" or "shemale":
        print(f"Good Afternoon {name}")


