# Write a program to calculate the grade of a student from his marks from the 
# following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F



user_marks = int(input("Enter your marks here: "))

if user_marks >= 90 and user_marks <= 100:
    print("Grade: Ex")
elif user_marks >= 80 and user_marks <= 90:
    print("Grade: A")
elif user_marks >= 70 and user_marks <=80:
    print("Grade: B")
elif user_marks >= 60 and user_marks <= 70:
    print("Grade: C")
elif user_marks >= 50 and user_marks <=60:
    print("Grade: D")
elif user_marks < 50:
    print("Grade: F")
else:
    print("Invalid Marks Entry!")