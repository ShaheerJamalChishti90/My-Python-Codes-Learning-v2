# import pyttsx3
 
# # init function to get an engine instance for the speech synthesis 
# mimi = pyttsx3.init() #initialize
 
# # say method on the engine that passing input text to be spoken
# mimi.say("Hello, Im Mimi from Indonesia, Im so intellegent and I have a loving and kind nature")
# print("Hello, Im Mimi from Indonesia, Im so intellegent and I have a loving and kind nature") 

# mimi.runAndWait()


import pyttsx3

# Initialize the engine
engine = pyttsx3.init()

# Get the available voices
voices = engine.getProperty('voices')

# Print all available voices
for index, voice in enumerate(voices):
    print(f"Voice {index}:")
    print(f"  ID: {voice.id}")
    print(f"  Name: {voice.name}")
    print(f"  Language: {voice.languages}\n")

# Set the desired voice (e.g., 0 for the first voice, 1 for the second, etc.)
engine.setProperty('voice', voices[0].id)  # Change to voices[1].id for another voice

# Test the voice
engine.say("Hello! This is a test of the pyttsx3 library.")
engine.runAndWait()
