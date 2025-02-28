# import random
user1name = input("USER01- Enter your name here: ").capitalize()
user2name = input("USER02- Enter your name here: ").capitalize()

user1points = 0
user2points = 0

options =  ["snake", "water", "gun"] 

while True:
    print('')
    user1option = input(f"{user1name} enter a choice (snake, water, gun): ").lower() 
    user2option = input(f"{user2name} enter a choice (snake, water, gun): ").lower() 
        
    if user1option == user2option:
            print('')
            print(f"Its a tie, {user1name} choose {user1option} and {user2name} also choose {user2option} ")
            
    elif user1option == 'snake' and user2option == 'water' or \
        user1option == 'water' and user2option == 'gun' or \
        user1option == 'gun' and user2option == 'snake':
            print('')
            print(f"{user1name} win, {user1name} choose {user1option} and {user2name} choose {user2option}")
            user1points += 1
            
    else:
            print('')
            print(f"{user2name} win, {user2name} choose {user2option} and {user1name} choose {user1option}")
            user2points +=  1
            
    def telling_points():
        print('')
        print(f"{user1name}'s points: {user1points}")
        print(f"{user2name}'s points: {user2points}")
    telling_points()
            
            
    def play_again():
            print('')
            print('Do you guys wanna play again?(yes/no)')
            play_again_user1 = input(f"{user1name}: ").lower()
            play_again_user2 = input(f"{user2name}: ").lower()
            

            if play_again_user1 == 'yes' and play_again_user2 != "yes":
                print('')
                print(f'{user1name}, {user2name} denied for playing again, to play again make em agree first')
                
            elif play_again_user1 != 'yes' and play_again_user2 == "yes":
                print('')
                print(f'{user2name}, {user1name} denied for playing again, to play again make em agree first')
                
            elif play_again_user1 != 'yes' and play_again_user2 != "yes":
                print('')
                print("Thanks for playing!")
            else:
                print('')    
                print("Invalid Input (yes/no)")
    play_again()              
    break
