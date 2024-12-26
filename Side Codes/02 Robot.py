import pyttsx3 #text to speed module
import math

# Initialize the pyttsx3 engine
engine = pyttsx3.init()

voices = engine.getProperty('voices')

def speak_with_david(text):
    engine.setProperty('voice', voices[0].id)  # Assuming David is the first voice
    engine.say(text)
    # engine.runAndWait()

# Define the robot's information
name = 'Mimi Robot'
model = 'Mimi from Indonesia 1.0'
manufacturer = 'Robotronics'
developer = 'Shaheer and Mimi'
variants = 'Jarvis 1.0 Basic, Jarvis 1.0 Pro, Jarvis 1.0 Enterprise'




def robot(name, model, manufacturer, query):
    if query == 'Name':
        response = f"My name is {name}"
    elif query == 'Model':
        response = f"My make Model  is {model}"
    elif query == 'Manufacturer':
        response = f"My manufacturer is {manufacturer}"
    elif query == 'Developer':
        response = f'My developer is {developer}'
    elif  query == 'Variants':
        response = f'Jarvis 1.0 comes in 3var different variants, {variants}'
    else:
        response = 'Invalid Input'
    
    # Speak the response
    speak_with_david(response)
    print(response)
    engine.runAndWait()

# Ask the user for their question
def asking_user01():

    speak_with_david('what would you like to know about me?')
    print('What would you like to know about me?')
    engine.runAndWait()
    user_query = input('\nName;\nModel;\nManufacturer;\nDeveloper;\nYour answer here: ').capitalize()

    # Call the robot function with the user query
    robot(name, model, manufacturer, user_query)
# asking_user01()

def asking_user02():
    while True:
        asking_user01()

        speak_with_david('Wana know something else?')
        print('Wana know something else?')
        engine.runAndWait()
        asking_user = input('Y/N: ').capitalize()

        if asking_user == 'N':
            # Ask the user for their question
            speak_with_david('ThankYou for having a great time with Jarvis')
            print('ThankYou for having a great time with Jarvis')
            engine.runAndWait()
            break

        elif asking_user != 'Y':
            speak_with_david('Invalid Input')
            print('Invalid Input')
            engine.runAndWait()
asking_user02()



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