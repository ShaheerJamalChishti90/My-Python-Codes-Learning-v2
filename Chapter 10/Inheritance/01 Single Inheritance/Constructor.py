class Company:
    language = "Js"
    package = '100K'

    def __init__(self, name, age): #"__init__" ek dunder method hai, ye automatically call hota hai 
        self.name = name
        self.age = age
        
employee = Company('Shaheer Jamal', '18')
employee.language = 'Python'
print(f'{employee.name} is an {employee.age} y/o {employee.language} developer, He earns {employee.package}/month')  

class Company:
    language = "Js"
    package = '100K'
    
employee = Company()
employee.name = 'Shaheer Jamal'
employee.age = '18'
print(f'{employee.name} is an {employee.age} y /o {employee.language} developer,He earns {employee.package}/month')