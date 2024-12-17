import pyttsx3

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

voices = engine.getProperty('voices')

def speak_with_david(text):
    engine.setProperty('voice', voices[0].id)  # Assuming David is the first voice
    engine.say(text)
    # engine.runAndWait()

# Define the robot's information
name = 'Jarvis'
model = 'Jarvis 1.0'
manufacturer = 'Robotronics'


developer = 'Shaheer'
variants = 'Jarvis 1.0 Basic, Jarvis 1.0 Pro, Jarvis 1.0 Enterprise'

def robot(name, model, manufacturer, query):
    if query == 'Name':
        response = f"My name is {name}"
    elif query == 'Model':
        response = f"My model is {model}"
    elif query == 'Manufacturer':
        response = f"My manufacturer is {manufacturer}"
    elif query == 'Developer':
        response = f'My developer is {developer}'
    elif query == 'Variants':
        response = f'Jarvis 1.0 comes in 3 different variants, {variants}'
    else:
        response = 'Invalid Input'
    
    # Speak the response
    speak_with_david(response)
    print(response)
    engine.runAndWait()

# Function to ask the user a question and call the robot function
def ask_user01():
    speak_with_david('What would you like to know about me?')
    print('What would you like to know about me?')
    engine.runAndWait()
    user_query = input('\nName;\nModel;\nManufacturer;\nDeveloper;\nVariants;\nYour answer here: ').capitalize()

    # Call the robot function with the user query
    robot(name, model, manufacturer, user_query)

# Function to keep asking the user until they say no
def asking_loop():
    while True:
        ask_user01()
        
        # Ask if they want to know something else
        speak_with_david('Wana know something else?')
        print('Wana know something else?')
        engine.runAndWait()
        asking_user = input('Y/N: ').capitalize()

        # If the user says no, break the loop
        if asking_user == 'N':
            speak_with_david('Thank you for having a great time with Jarvis.')
            print('Thank you for having a great time with Jarvis.')
            engine.runAndWait()
            break
        elif asking_user != 'Y':
            print("Invalid Input. Please type 'Y' or 'N'.")
    
asking_loop()

speak_with_david('I can also perform some mathematical tasks, Do you wanna perform any mathematical task? (yes/no):')
print("I can also perform some mathematical tasks,Do you wanna perform any mathematical task? (yes/no): ")
engine.runAndWait()
maths_task = input('answer here: ').lower()

if maths_task == 'yes':

    def perform_math_task(operation, num1, num2):
        if operation == 'add':
            return num1 + num2
        elif operation == 'subtract':
            return num1 - num2
        elif operation == 'multiply':
            return num1 * num2
        elif operation == 'divide':
            if num2 == 0:
                return "Error: Division by zero"
            return num1 / num2
        else:
            return "Error: Unsupported operation"

# Example usage
# operation = 'add'  # choose between 'add', 'subtract', 'multiply', 'divide'
# num1 = 10
# num2 = 5

    num1 = int(input("Enter 1st number here: "))
    operation = input("What operation would you like to perform (add, multiply, subtract, divide): ")
    num2 = int(input("Enter 2st number here: "))

    result = perform_math_task(operation, num1, num2)
    speak_with_david(f'The result of {operation} operation is: {result}')
    print(f"The result of {operation} operation is: {result}")
    engine.runAndWait()



def speak_with_zira(text):
    engine.setProperty('voice', voices[1].id)  # Assuming Zira is the second voice
    engine.say(text)
    # engine.runAndWait()

speak_with_zira('Would yu like to read the Development Overview of Jarvis AI Robot:')
print('Would yu like to read the Development Overview of Jarvis AI Robot: ')
engine.runAndWait()
robot_discription = input('Y/N: ').capitalize()



if robot_discription == 'Y':
    speak_with_zira('''
Jarvis AI Robot Development:

The Jarvis AI robot was meticulously developed by Robotronics, a pioneer in robotics and AI technology. The project was undertaken at the Karachi Institute of Technology (KIT), under the expert supervision of Sir Ibrahim. The development environment was state-of-the-art, incorporating the latest advancements in AI algorithms, robotics engineering, and smart technology integration. This collaborative effort, led by Muhammad Shaheer Jamal, resulted in a versatile and intelligent robot capable of performing a wide range of tasks with precision and efficiency.''')
    print('''
Jarvis AI Robot Development:

The Jarvis AI robot was meticulously developed by Robotronics, a pioneer in robotics and AI technology. The project was undertaken at the Karachi Institute of Technology (KIT), under the expert supervision of Sir Ibrahim. The development environment was state-of-the-art, incorporating the latest advancements in AI algorithms, robotics engineering, and smart technology integration. This collaborative effort, led by Muhammad Shaheer Jamal, resulted in a versatile and intelligent robot capable of performing a wide range of tasks with precision and efficiency.''')
    engine.runAndWait()
else:
    speak_with_zira('No worries at all! If you’d prefer, I can give you a brief summary or highlight the key points. Just let me know what works best for you!')
    print('No worries at all! If you’d prefer, I can give you a brief summary or highlight the key points. Just let me know what works best for you!')
    engine.runAndWait()