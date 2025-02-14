from pynput.keyboard import Key, Controller
import time

message = "Mishkatt!"
keyboard = Controller()

time.sleep(8)

for i in range(100):
    for letter in message:
        keyboard.press(letter)
        keyboard.release(letter)
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)
    # time.sleep(0.5)
