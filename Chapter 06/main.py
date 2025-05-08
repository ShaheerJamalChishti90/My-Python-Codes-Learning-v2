# # 2. Write a program that asks for years of service and qualification
# # and calculates the salary as per the given table.
# y = int(input("Enter your years of service: "))
# q = input("Enter your qualification (Masters/Bachelors): ").capitalize()

# if y >= 10: 
#     if q == "Masters":
#         s = 150000
#     elif q == "Bachelors":
#         s = 100000
#     else:
#         s = "Invalid qualification"
# elif y < 10:
#     if q == "Masters":
#         s = 100000
#     elif q == "Bachelors":
#         s = 70000
#     else:
#         s = "Invalid qualification"
# else:
#     s = "Invalid input for years of service"

# if isinstance(s, int):
#     print(f"Your salary is: {s}")
# else:
#     print(s)

s = "Shaheer"
if isinstance(s, str):
    print(True)
else:
    print(False)