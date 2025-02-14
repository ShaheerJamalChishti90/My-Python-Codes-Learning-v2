# Create a class BankAccount with a private attribute _balance. Implement getter and setter methods to access and modify the balance, ensuring that the balance cannot be set to a negative value.
# Inheritance and Encapsulation

class BankAccount:
    def __init__(self):
        self._balance = 0
        

class ModifyBalance(BankAccount):
    def __init__(self):
        super().__init__()

    @property
    def balance(self):
        return f'This is your account balance: {self._balance}$'
    
    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError('Amount cant be negative!')
        else:
            self._balance = amount


bank_account = ModifyBalance()
bank_account.balance = int(input("Enter the amount here: "))
print(bank_account.balance)



    

    