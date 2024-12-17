# 2. The game() function in a program lets a user play a game and returns the score 
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
# contains the previous Hi-score. You need to write a program to update the Hi-score whenever the game() function breaks the Hi-score


# Iss code ke end mein pehle mein file ko write mode mein open kar raha hoon uske baad check kar raha hoon ke kia current score hiscore se ziyada hai ya nahi jiski wajha se code sahi kaam nahi kar raha

import random
def game():
    
    print("You are in a match....")
    current_score = random.randint(1, 100)
    print(f"Well Played, you scored {current_score}")

    with open("Chapter 09\\Practice Set\\user_score.txt") as file:
        hiscore = file.read()

    if hiscore != "":
        hiscore = int(hiscore)
    else:
        hiscore = 0

    # if hiscore == '':
    #     hiscore = 0
    # else:
    #     hiscore = int(hiscore)

    with open("Chapter 09\\Practice Set\\user_score.txt", "w") as file:
        if current_score > hiscore:
            file.write(str(current_score))
            print("You have broken the Hi-score")
            
    return current_score
game()
        
    



# import random

# def game():
    
#     print("You are playing the game....")
#     score = random.randint(1, 100) 
#     print(f"YOUR HI-SCORE IS: {score}")
    
#     # lets open a file now to store the user hi-score
#     with open("hi_score.txt", "a") as file:
#         score_file = file.write(str(score))
        
#     if score > score_file:
#         with open("hi_score.txt", "w") as file:
#             file.write(str(score))
#     return score
# game()

# Iss code ke end mein pehle mein check kar raha hoon ke kia current score hiscore se ziyada hai ya nahi, agar ziyada hai tou wo file open karega aurr usmein hiscore ko current score se overwrite kardega


import random

def game():
    
    print("you re playing the game....")
    score = random.randint(1, 100)
    
    with open('Chapter 09\\Practice Set\\hiscore.txt') as f:
        hiscore = (f.read())
        
    if hiscore == "":
        hiscore = 0
    else:
        hiscore = int(hiscore)
        
    print(f'your score is = {score}')
    
    if score > hiscore:   
        with open('Chapter 09\\Practice Set\\hiscore.txt', 'w') as f:
            f.write(str(score))
    
    return score
game()
        
