# class Employee:
#     company = "Google" # Specific to Each Class
#     experience = "15 years"
#     hands_on = 'python'
    
# harry = Employee() # Object Instatiation
# harry.company
# Employee.company = "YouTube" # Changing Class Attribute

# # harry.hands_on
# # Employee.hands_on = 'Full stack'


# print(Employee.company)
# # print(Employee.hands_on)
# # print(harry)



class Ceo:
    company = "Google"
    salary = 50000
    hands_on = 'python'
    
    
Ceo.hands_on = "Full Stack"
shaheer = Ceo() 

print(shaheer.hands_on)


class Car:
    def __init__(self, color):
        self.color = color
    
    def start(self):
        print("Car started")

my_car = Car("red")
my_car.start()

        