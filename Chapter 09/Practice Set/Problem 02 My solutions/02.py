# 2. The game() function in a program lets a user play a game and returns the score 
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
# contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score

import random
import datetime

time_now = datetime.datetime.now()

def game():
    user_point = 0
    computer_point = 0
    
    while True:
        computer_guess = random.randrange(1, 11)
        user_input = int(input("Enter your guess here (1-10): "))

        if user_input not in  range(1, 11):
            print(f'{user_input} is out of range 1-10,  pls enter the correct number: ')
            continue


        if user_input != computer_guess:
            print(f'\nUser Guessed = {user_input} || Computer Guessed = {computer_guess}\nComputer Win!')
            computer_point += 1
        else:
            print(f'\nUser Guessed = {user_input} || Computer Guessed = {computer_guess}\nUser Win!')
            user_point += 1
            
            
        with open("Chapter 09\\Practice Set\\score.txt", 'a') as scores:
            scores.write(f'\n{time_now.strftime("%A, %d %b %Y")} {time_now.strftime("%I:%M %p")}"\nUser Score: {user_point} || Computer Score: {computer_point}\n')
        
            
            
        print("\nBelow is the Score File:")
        with open("Chapter 09\\Practice Set\\score.txt", 'r') as scores:
            print(scores.read())
            
            # Ask to play again
        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("\nBelow is the Final Score File:")
            with open("Chapter 09\\Practice Set\\score.txt", 'r') as scores:
                print(f"{scores.read()}\nThis game was played on:\n{time_now.strftime("%A, %d %b %Y")} at {time_now.strftime("%I:%M %p")}")
            break      
        
  
        
        
game()