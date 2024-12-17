import pyjokes
joke = pyjokes.get_joke()
print(joke)


import pyttsx3
engine = pyttsx3.init()
engine.say("I can fix all those lies Oo Baby babes i run but im running to you")
engine.runAndWait()

import os

# Specify the directory path you want to start listing from
start_path = "D:\\"  # Replace with your desired starting directory, like C:\ or D:\


# Walk through the directory tree
for dirpath, _, _ in os.walk(start_path):
    print(dirpath)


import time

for i in range(1, 10 + 1):
    sleepy_time = time.sleep(2)
    print("I'm sleepy", i)
    i = i + 1
print("I'm Dead!")


