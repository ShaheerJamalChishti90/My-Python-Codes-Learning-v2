# number_list = [10, 11, 12, 13, 14] 

# for x in number_list:
#     if (x%x and x%1) == 0:
#         print(f'{x} is prime')
#         break
#     else:
#         print(f'{x} is not prime')
#         break

number_list = [10, 11, 12, 13, 14]

for x in number_list:
    if x <= 1:
        print(f'{x} is not prime')
    else:
        is_prime = True
        # Check divisibility from 2 to x-1
        for i in range(2, x):
            if x % i == 0:
                is_prime = False
                break
        if is_prime:
            print(f'{x} is prime')
        else:
            print(f'{x} is not prime')
