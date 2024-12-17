#Scenario A: Different from the Below Scenarios 
#Simple concept of Object Oriented Programming
class Employee:  
    def  __init__(self, exp, salary):  #Instance Attributes
        self.exp = exp
        self.salary = salary
        
    def info(self): #Instance Method
        print(f'Employee has {self.exp} years of experience and earns {self.salary} rupees')
        
shaheer = Employee(2, 250000) #Class Object/Instance
shaheer.info() #Calling Class Object
        

#Scenario 1:

class Finance: #Class with no private attributes: cons: attributes can be manipulated easily and can be accessed directly 
    def __init__(self):
        self.revenue = 12000000
        self.sales = 98000

Finance_Dept = Finance() #Class Instance 
print(Finance_Dept.__dict__) 

class HR: #Another class with no private attributes
    def __init__(self):
        self.employees = 50
        self.salary = 75000
        Finance_Dept.revenue = 20000000 #Accessing the Upper Class's Attribute (Revenue) which is not technically good when doing encapsulation
        # print(Finance_Dept.revenue) #Here we can print the manipulated attribute easily without any problem
        

HR_Dept = HR() #Class Instance
print(Finance_Dept.__dict__)


#Scenario 2:

class Finance: #Base Class
    def __init__(self): #Hardcoding the attributes values and making them PRIVATE
        self.__revenue = 12000000 #They cant be accessed outside the class, they are the protected ones
        self.__sales = 98000

finance = Finance()
print(finance._Finance__revenue) #The protected attributes can be access in this way