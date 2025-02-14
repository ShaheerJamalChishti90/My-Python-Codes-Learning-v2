class Piggybank:
    def __init__(self):
        self.__money = 0

    def add_money(self, money: int):
        if money >= 0:
            self.__money =+ money #self.__money = self.__money + money
        else:
            print("Invalid amount")
            
    def get_money(self):
        return f"You've total {self.__money}$ in your Piggybank!"


amount = int(input("Enter the amount to add: "))

gullaq = Piggybank()

gullaq.add_money(amount)
print(f'You have added {amount}$ to your piggybank')

print(gullaq.get_money())
    





        