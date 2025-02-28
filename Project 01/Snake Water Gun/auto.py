import random

options =  ["snake", "water", "gun"] 

def game():
    while True:
        user_option = input("Enter a choice (snake, water, gun): ").lower()
        computer_option = random.choice(options) 
        
        if user_option == computer_option:
            print(f"Its a tie, User choose {user_option} and Computer also choose {computer_option} ")
        elif user_option == 'snake' and computer_option == 'water' or \
            user_option == 'water' and computer_option == 'gun' or \
            user_option == 'gun' and computer_option == 'snake':
            print(f"User win, User choose {user_option} and computer choose {computer_option}")
        else:
            print(f"Computer win, User choose {user_option} and computer choose {computer_option}")
            
        play_again = input('Do you want to play again? (yes/no): ')
        if play_again.lower() != 'yes':
            print("Thanks for playing")
            break
game()