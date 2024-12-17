# n = int(input("Enter the number here: "))

# if n not in range(0, 21):
#     print("Invalid Input!")

# elif n % 2 != 0:
#     print('Odd Number, Weird!')

# elif (n % 2 == 0) and n in range(2, 6):
#     print('2 =< Even Number =< 6, Not Weird!')

# elif (n % 2 == 0) and n in range(6, 21):
#     print('6 =< Even Number =< 20, Weird')

# elif n % 2 == 0 and n > 20:
#     print('Even Number > 20, Not Weird!')
    
# else: 
#     print('Fucn You!')


n = 5

bla = [i for i in range(n)]
# bla02 = [i**2 for i in bla]
print(f'List before squaring: {bla}')
print('\nNumbers after squaring: ')
for i in bla:
    bla02 = i**2
    
    print(bla02)


