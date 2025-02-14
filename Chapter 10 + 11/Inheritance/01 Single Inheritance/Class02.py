class Shaheer_Tech_Group: #This is a Class/Blueprint
    #These are the CLASS ATTRIBUTES as they directly belongs to the class
    language = 'Python'   
    package = 125000
    

#One thing to remember, Instance/Object Attribute always take Preference over Class Attribute

#Instance/Object Attribute  Class Attribute pe fauqiyat  rakhta hai
    
employee = Shaheer_Tech_Group() #This is an Object made from Class
employee.name = 'Aliyaan' #This is an Object/Instance Attribute

print(f'{employee.name} works as a {employee.language} Developer in Shaheer Tech Group, He earns {employee.package}/month\n')

employee02 = Shaheer_Tech_Group() #This is an Object made from Class
employee02.name = input("Enter your name here: ")         #This is an Object/Instance Attribute

print(f'{employee02.name} joined Shaheer Tech Group on Wednesday as an Intern, he will learn {employee02.language} and he will  be paid {employee02.package}/month')