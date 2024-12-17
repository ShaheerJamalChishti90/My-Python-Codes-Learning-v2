class Company: #This is a Class
    #Below are the Class Attributes
    language = 'Python'
    package = "100K"
    
    
    def Worker_Info(self): #This is a Function (ye self jo hai object se link hai)
        print(f'{self.language} Developers earns {self.package} per month')

    @staticmethod
    def Greet():
        print("Good Morning!")
    
    
worker = Company() #This is an Object created from Class
worker.name = 'Shaheer' #This is an Instance/Object Attribute
worker.Greet()
print(f'This is {worker.name}, I work as a {worker.language} Developer')
        
worker.Worker_Info()
# Company.Worker_Info(worker)
