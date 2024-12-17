def say_hello():
    print("Hello, world!")
    return ("Hey Paksitan, Hellow Karachi")
print(say_hello())

# Quick Quiz: Write a program to greet a user with “Good day” using functions
def  greet_user():
    user_name = input("Enter your name here: ")
    return f"Hellow Mr/Ms {user_name}"
print(greet_user())  # Output: Hellow Mr/Ms <your_name>  #




# Adding two inputs by two different ways of def function:
# way 01:

a = int(input("Number 01: "))
b = int(input("Number 02: "))

def addition(a, b):
    return (f'The sum of {a} and {b} is {a + b}')

print(addition(a, b))  

# way 02:

def add():
    a = int(input("Number 01: "))
    b = int(input("Number 02: "))

    addition = (a + b)
    print(addition)

add()


 


# Taking average of 2 numbers:

def average():
    a = int(input("number 01 = "))
    b = int(input("number 02 = "))
    c = int(input("number 03 = "))

    avg = (a + b + c)/3 
    print(avg)

average()
average()
average()

a = int(input("number 01 = "))
b = int(input("number 02 = "))
c = int(input("number 03 = "))

def  average():
    return ((a + b + c)/3)
print(f"The average of {a}, {b} and {c} is {average()}")


# GPT CODE RENEWED BY ME INTO EVEN CHECKER5

# Example usage:
numbers = [1, 2, 3, 4, 5]

def process_numbers(numbers):
    total = 0
    for integer in numbers:
        if integer % 2 == 0:  # Check if the number is even
            total += integer  # Add the odd number to the total
    return total
result = process_numbers(numbers)
print(result)  # for even it'll be 6


#CHAT GPT CODE (SUM OF ODD NUMBERS)

def process_numbers(numbers):
    total = 0
    for number in numbers:
        if number % 2 != 0:  # Check if the number is odd
            total += number  # Add the odd number to the total
    return total
# Example usage:
numbers = [1, 2, 3, 4, 5]
result = process_numbers(numbers)
print(result)  # Output will be 9 (1 + 3 + 5)



name = input("Enter your name here: ")
# name = ["shaheer", "jamal", "chishti"]

def greet():
    message = f"Hello, {name}!"
    return message

print(greet())


class ToyRobot:
    def __init__(self, color, battery_level):
        self.color = color
        self.battery_level = battery_level

# Creating a new ToyRobot
my_robot = ToyRobot("Green", 100)

# Checking the robot's details
print(f"My robot is {my_robot.color} and has a battery level of {my_robot.battery_level}.")




class Infinix:
    def __init__(self, color, battery_level):
        self.color = color
        self.battery_level = battery_level

my_phone = Infinix("Black", 85)

print(f"I've an Infinix phone, its color is {my_phone.color} and rn its battery level is {my_phone.battery_level}")






mycar = input("Which car you have?: ")
color = input("Car color: ")
model = input("Car model: ")
prize = input("Car prize: ")
company = input("Car company: ")


class car:
    def __init__(self, color, model, prize, company,):
       
        self.color = color
        self.model = model 
        self.prize = prize
        self.company = company

car_details = car(color, model, prize, company )

print(f"I've a car, its a {car_details.company} {mycar}, I bought it for {car_details.prize}, its in {car_details.color} color and its make model variant is {car_details.model} ")


## Taking MEAN/MEDIAN/MODE of the numbers given by the user:


asking_user = int(input("What would you like to calculate?\n01- Mean\n02- Median\n03- Mode\nYour answer here: "))
if asking_user == 1:
    print("Enter the values below to calculate Mean:")

    a = int(input("Enter the first number here: "))
    b = int(input("Enter the second number here: "))

    def FuncMean(a, b):
     return(a  + b)/2
    print(f"The Mean is {FuncMean(a, b)}")


elif asking_user == 2:
    a = input("Enter the first number: ") 
    b = input("Enter the second number: ") 
    c = input("Enter the third number: ") 
    
    def FuncMedian(a, b, c):
       return sorted([a, b, c])[1]
    print(f"The Median  is {FuncMedian(a, b, c)}")

elif asking_user == 3:
   a = input("Enter the first number: ")
   b = input("Enter the second number: ")
   c = input("Enter the third number: ")
   d = input("Enter the fourth number: ")

   def FuncMode(a,b,c,d):
        return max(a,b,c,d)
   print(f"The Mode is {FuncMode(a, b, c, d)}")

else:
    print("Invalid choice")



# Get user input
user_input = input("Enter multiple integers separated by space: ")

# Split the input string into a list of integers
numbers = [int(x) for x in user_input.split()]

# Print the list of numbers
print(numbers)




status = int(input('Enter the server status here: '))
def http_status(status):
    match status:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Internal Server Error"
        case _:
            return "Unknown status"
print(http_status(status))

