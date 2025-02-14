# Protecting Attributes:
# Create a BankAccount class with a protected attribute _balance.
# Write a method deposit(amount) to add money and withdraw(amount) to subtract money (only if there’s enough balance).

class Bankaccount:
    def __init__(self):
        self._balance = 0

    def Deposite(self):
        amount = int(input("Enter the amount to deposit: "))
        self._balance += amount
        
    def Withdraw(self):
        amount = int(input("Enter the amount to withdraw: "))
        if self._balance >= amount:
            self._balance -= amount
            print(f"Here is your money: {amount}")
        else:
            print("You don't have enough money in your account")
            
shaheer = Bankaccount()
shaheer.Deposite()
shaheer.Withdraw()
