# Extend the BankAccount class from earlier to include a method that allows deposits and withdrawals, ensuring that the account balance cannot go below zero and that deposits must be positive.



class BankAccount: 
    def __init__(self):
        self.__balance = 0

    #decorator for deposite
    @property
    def deposite(self):
        return f"{self.__balance}$ Deposited!"
    
    @deposite.setter 
    def deposite(self, amount):
        if amount < 0:
            raise ValueError("Deposites can not be negative!")
        else:
            self.__balance += amount #self.__balance = self.__balance + amount
            
    
    #decorator for withdrawal
    @property
    def withdrawal(self):
        return f"{self.__balance}$ Withdrawn!"
        
    @withdrawal.setter
    def withdrawal(self, amount):
        if amount < 0:
            raise ValueError("Withdrawals can not be negative!")
        else:
            if amount > self.__balance:
                raise ValueError("Insufficient funds!")
            else:
                self.__balance -= amount #self.__balance = self.__balance - amount
        
        
    #decorator to check account balance
    @property
    def check_balance(self):
        return f"Account balance: {self.__balance}$"
        
    @check_balance.setter
    def current_balance(self):
        self.__balance = self.__balance

shaheers_account = BankAccount()
print("\n1. Deposit\n2. Withdraw\n3. Account Balance\n4. Exit")
user = int(input('Enter here: '))

while True:
        if user == 1:
            depo_amount = int(input("Enter the amount to deposit: "))
            shaheers_account.deposite = depo_amount
            print(shaheers_account.deposite)
            break
        
        elif user == 2:
            wid_amount = int(input("Enter the amount to withdraw: "))
            shaheers_account.withdrawal = wid_amount
            print(shaheers_account.withdrawal)
            break
            
        elif user == 3:
            print(shaheers_account.check_balance)
            break


        elif user == 4:
            print('Thanks for having our service')
            break
        
        else:
            print('Invalid input!')
            break
