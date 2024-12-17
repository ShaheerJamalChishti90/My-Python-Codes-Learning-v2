import random

def game():
    computer_input = random.randint(1, 10)
    user_input = int(input("Choose any number (0-10): "))
    
    user_points = 0
    computer_points = 0

    if computer_input != user_input:
        print(f'Computer chose: {computer_input} || User chose: {user_input}\nComputer Win!')
        computer_points += 1
    else:
        print(f'Computer chose: {computer_input} || User chose: {user_input}\nUser Win!')
        user_points += 1

    with open("Chapter 09\\Practice Set\\score02.txt", "a") as f:
        if computer_input != user_input:
            f.write(f"\nComputer Wins!\nUser points: {user_points} || Computer points: {computer_points}")
        else:
            f.write(f"\nUser Wins!\nUser points: {user_points} || Computer points: {computer_points}")

    with open("Chapter 09\\Practice Set\\score02.txt") as f:
        f.read()
game()