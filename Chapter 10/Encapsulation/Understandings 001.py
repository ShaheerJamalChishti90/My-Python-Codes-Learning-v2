#Scenario 1

# class Finance: #This is the first class of Finance Dept, all the data/attributes are publix in this class which can be easily accessed by anyone outside tne Finance Class

#     def __init__(self):
#         self.revenue = 150000 #Public Attributes
#         self.sales = 2500

# dept_fin = Finance()

# class HR: #This is the second class of HR Dept, anyone can access/manipulate the data of upper class into this class 
#     def __init__(self):
#         self.employees = 25 #This class also have public attributes 
#         self.salary = 45000
#         dept_fin.revenue = 125000 #This is the data of Finance Department which is accessed in the HR Dept.. and is also manipulated

# dept_hr = HR()
# print(dept_fin.revenue) #Here i can print the manipulated value of revenue of Finance Class and thats not quite right







#Scenario 2
#Majoirity of the things are same in this scenario, the difference is, here i made the Finance attribute private 
class Finance: 
    def __init__(self):
        self.__revenue = 150000 #Private Attributes
        self.__sales = 2500

dept_fin = Finance()

class HR: 
    def __init__(self):
        self.employees = 25  
        self.salary = 45000
        dept_fin.__revenue = 125000 #When Im trying to access and manipulate the data of the Finance Dept..., it aint gona work  
dept_hr = HR()
print(dept_fin.__revenue)  #Here im trying to print the revenue of but its throwing an error because of the Privacy  
