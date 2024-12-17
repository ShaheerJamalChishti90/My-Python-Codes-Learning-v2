# Q2: Write a program to fill in a letter template given below with name and date.

import time

current_tdm = time.strftime("%c")

name = input("Enter your name here: ")

letter = f'''
        Dear {name},
        This is a letter to you.
        your are selected in IBX Global!
        Date: {current_tdm}
'''

print(letter)
