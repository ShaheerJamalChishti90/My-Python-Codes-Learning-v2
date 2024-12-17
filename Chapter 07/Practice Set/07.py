# # Write a program to print the following star pattern.
# # *
# # ***
# # ***** for n = 3


# a = "*"
# i = 1

# while i <= 3:
#     print(a) 
#     i += 1 # i = i + 1
#     a += a # a = a + a

a = "*"
for i in range(3):
    print(a)     #or    # print(a * i)
    a += "*"     #or  # a =  a+ a




   

# star = "*"
# for i in range(3):
#     i * star
#     print(star)
    



# n = 3
# for i in range(n):
#     stars = '*' * (2 * i + 1)
#     print(stars.center(2*n))
# print("")


# n = 3
# for i in range(n):
#    stars = '*' * (i * 2 + 1)
#    spaces = ' ' * (n - i)
#    print(spaces + stars + spaces)

   

# n = int(input('number: '))

# for i in range(1, n+1):
#     if(i == 1 or i == n):
#         print("*" * n, end="")
#     else:
#         print("*", end="")
#         print(" " * (n - 2), end="")
#         print("*", end="")
#     print("")

'''
i = 1 and n = 5

if:
    i = 1 or i(1/2/3/4/5) = 5
        * x 5 = *****
else:
    * 
    " " x (n - 2) # 3 spaces print hoengy jab tak loop chalega
'''

# spaces = '_' * (3 - 2 - 1)
# print(spaces)






         






