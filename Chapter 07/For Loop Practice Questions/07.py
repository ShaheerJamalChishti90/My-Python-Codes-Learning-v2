# Number of Vowels: Write a program that counts the number of vowels in a string entered by the user using a for loop.

vow_entry = input('Enter anything here: ').lower()
vow = ['a', "e", 'i', 'o', 'u']
count = 0

for i in vow_entry:
    if i in vow:
        count += 1
print(f'There are {count} vowels in your string')

         