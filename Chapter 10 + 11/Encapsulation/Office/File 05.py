class Boy:
    def __init__(self, salary):
        self.__salary = salary
        
    def get_salary(self):
        print(self.__salary)
    def set_salary(self, amount):
        if amount < 0:
            raise ValueError('Amount can not be in negative')
        else:
            self.__salary = amount
            
    money = property(get_salary, set_salary)

shaheer = Boy(100)
# shaheer.money 
shaheer.money = 200 #Changing the value here
shaheer.money

    