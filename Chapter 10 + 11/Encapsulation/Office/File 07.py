class Company:
    def __init__(self, salary):
        self.__salary = salary
        
        
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self.__salary = value


company = Company(1000)
company.salary = 2000
print(company.salary)