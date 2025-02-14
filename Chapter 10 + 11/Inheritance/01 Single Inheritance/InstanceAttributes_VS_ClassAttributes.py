class Company:  #This is a Class and below are Class Attributes
    package = 150000
    language = "Js"


Shaheer = Company() #This is an  Object made from Class
#these all  are the Instance Attributes which takes over the Class Attributes
Shaheer.name = 'Shaheer' 
Shaheer.language = "Py"
Shaheer.package = 200000

print(f'{Shaheer.name} works in a Company as a {Shaheer.language} Developer where he is paid {Shaheer.package}\n')

Alina = Company() #This is an  Object made from Class and Below are the Class and Instance Attributes
Alina.name = "Alina"
print(f'{Alina.name} works  in the same company but  as a {Alina.language} developer and she is paid {Alina.package}')