class Boy:
    def __init__(self):
        self.__salary = 0 
        
    @property
    def salary(self):
        return f"This is your salary: {self.__salary}"

    @salary.setter
    def salary(self, salary):
        if salary < 0:
            raise ValueError("Salary cannot be negative")
        else:
            self.__salary = salary
    
shaheer = Boy()
shaheer.salary = 1000
print(shaheer.salary)