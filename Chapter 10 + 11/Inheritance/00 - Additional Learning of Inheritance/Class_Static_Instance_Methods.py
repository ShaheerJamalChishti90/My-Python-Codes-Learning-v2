class Company: #This is a Class
    #Below are the Class Attributes
    language = 'Python'
    package = "100K"
    
    
    def Worker_Info(self): #This is a Function (ye self jo hai object se link hai)
        print(f'{self.language} Developers earns {self.package} per month')

    @staticmethod
    def Greet():
        print("Good Morning!")
     
     
    @staticmethod   
    def techfirm():
        print("Welcome to TECH FIRM\nTech Firm is a leading IT company")
    
    @staticmethod
    def addnumbers(*numbers: int):
        return sum(numbers)
    
worker = Company() #This is an Object created from Class
worker.name = 'Shaheer' #This is an Instance/Object Attribute
worker.package = "200K USD"
worker.Greet()
worker.techfirm()
print(f'This is {worker.name}, I work as a {worker.language} Developer')
worker.Worker_Info()
print(f"Recently {worker.name} earned {worker.addnumbers(900, 50)}K PKR through stocks")
# Company.Worker_Info(worker)