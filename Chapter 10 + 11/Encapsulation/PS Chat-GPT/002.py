# Create a Gym class with a private attribute membership.
# Write a method buy(membership) to buy  a membership and sell(membership) to sell or reclaim your money back.

class Gym:
    def __init__(self):
        self.__membership = False  #This means that i currently dont hold a membership
        print("Welcome to the Gym. You currently dont have a membership")

    def buy(self):
        self.__membership = True    #This means that i have bought a membership and its gonna update the value in __init__ method
        print("Membership bought successfully")
        
    def sell(self):
        if self.__membership:  #This comes from the __init__ method
            self.__membership = False #This means that i have sold my membership again and gona update the value in __init__ method
            print("Membership sold successfully")
        else:
            print("No membership to sell")

gym_member = Gym()

while True:
    print("0. Check your Membership status")
    print("1. Buy Membership")
    print("2. Sell Membership")
    print("3. Exit\n")

    user_input = int(input("\nEnter your choice: "))

    if user_input == 0:
        print(gym_member._Gym__membership)
    elif user_input == 1:
        gym_member.buy()
    elif user_input == 2:
        gym_member.sell()
    elif user_input == 3:
        print('Thankyou for using our service')
        break
    else:
        print('Invalid choice. Please choose a valid option')
