# # Write a program to find out whether a student has passed or failed if it requires a 
# # total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.


# # taking marks from the student

# mark1 = float(int(input("Enter your English marks: ")))
# mark2 = float(int(input("Enter your Maths marks: ")))
# mark3 = float(int(input("Enter your Urdu marks: ")))

# # converting marks into percentage

# mark1_percentage = (mark1)/100 * 100
# mark2_percentage = (mark2)/100 * 100
# mark3_percentage = (mark3)/100 * 100

# # checking if the student pass the papers or not


# if mark1_percentage >= (33)/100 * 100:
#     print("You have passed in English")
# else:
#     print("You have failed in English")
# if mark2_percentage >= (33)/100 * 100:
#     print("You have passed in Maths")
# else:
#     print("You have failed in Maths")
# if mark3_percentage >= (33)/100 * 100:
#     print("You have passed in Urdu")
# else:
#     print("You have failed in Urdu")    

# # preparing the total percentage of 3 papers of student 

# total_percentage = (mark1 + mark2 + mark3)/300 * 100

# # final stage, checking if his percentage is higher than 40% or not

# if total_percentage >= (40)/100 * 100: 
#     print(f'Congraguations you have promoted to next class, your percentage is {total_percentage}%')
# else:
#     print(f'You are failed, try hard next time and must believe in yourself that you can do it, your percentage is {total_percentage}%')


# CHAT-GPT CORRECTED CODE:

# taking marks from the student
mark1 = float(input("Enter your English marks: "))
mark2 = float(input("Enter your Maths marks: "))
mark3 = float(input("Enter your Urdu marks: "))

# checking if the student passed in each subject
passed_subjects = True  # Assume the student passes all subjects

if mark1 < 33:
    print("You have failed in English")
    passed_subjects = False
else:
    print("You have passed in English")

if mark2 < 33:
    print("You have failed in Maths")
    passed_subjects = False
else:
    print("You have passed in Maths")

if mark3 < 33:
    print("You have failed in Urdu")
    passed_subjects = False
else:
    print("You have passed in Urdu")

# calculating the total percentage
total_percentage = (mark1 + mark2 + mark3) / 300 * 100

# final stage, checking if the student passed overall
if total_percentage >= 40 and passed_subjects:
    print(f'Congratulations, you have been promoted to the next class. Your percentage is {total_percentage:.2f}%.')
else:
    print(f'You have failed. Try harder next time and believe in yourself. Your percentage is {total_percentage:.2f}%.')
