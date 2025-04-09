from cmath import phase
import time
import speech_recognition as sr
import pyttsx3 
import webbrowser
import musiclib


recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def process_command(c):
    if "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com/")
    elif "open google" in c.lower():
        webbrowser.open("https://www.google.com/")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com/")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com/")
    elif "open netflix" in c.lower():
        webbrowser.open("https://www.netflix.com/")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclib.music[song]
        webbrowser.open(link)

if __name__ == "__main__":
    # engine.say("Hello, I am your assistant. How can I help you?")
    print("Initializing Jarvis...")
    speak("Initializing Jarvis...")

    while True: # Continuously listen for commands
        r = sr.Recognizer() # Create a recognizer object
        print("Recognizing...")
        
        try: # Try to recognize the audio
            with sr.Microphone() as source: # Use the microphone as the audio source
                print("Im listening, Speak now...") # Print a message to let the user know that the assistant is ready to listen
                speak("Im listening, Speak now...") # Print a message to let the user know that the assistant is ready to listen
                audio = r.listen(source, timeout=2, phrase_time_limit=1) # Listen for the audio via the microphone
            
            word = r.recognize_google(audio) # Use the google speech recognition service
            if(word.lower() == "python"):
                print(f"You said: {word}") # Print the command to the console
                print("Ya")
                speak("Ya")

                with sr.Microphone() as source: 
                    print("Jarvis active!.") 
                    speak("Jarvis active!") 
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    process_command(command)
                    # speak("This is just a test model! thansk for using it")

        except sr.UnknownValueError: # If the speech is unintelligible or can't be recognized, print this message
                print("Sorry, I did not get that, try to speak again...") 
                speak("Sorry, I did not get that, try to speak again...") 

        except sr.RequestError as re: # If there is a problem with the API, print this message
                print(f"Sorry, my speech service is down - {re}")
                speak(f"Sorry, my speech service is down - {re}")
            
    