import tkinter as tk
import random
import time
# Read sentences from file
with open("sentences.txt") as f:
    lines = f.readlines()
# Pick one sentence randomly
line = random.choice(lines).strip()
start = 0  # To store start time
# Function to start typing
def start_typing():
    global start
    entry.delete(0, tk.END)  # Clear input box
    result.config(text="")   # Clear result
    start = time.time()      # Start timer
    show_sentence.config(text=line)  # Show the sentence
# Function to check typing
def check():
    end = time.time()
    typed = entry.get()
    total_time = round(end - start, 2)
    # Accuracy calculation
    given = line.split()
    typed_words = typed.split()
    correct = sum(1 for a, b in zip(given, typed_words) if a == b)
    total = len(given)
    accuracy = round((correct / total) * 100, 2)
    result.config(text=f"Time: {total_time} sec\nAccuracy: {accuracy}%")
    # Save result in file
    with open("results.txt", "a") as file:
        file.write(f"Sentence: {line}\nTyped: {typed}\nTime: {total_time} sec | Accuracy: {accuracy}%\n\n")
# GUI setup
root = tk.Tk()
root.title("Typing Tutor")
root.geometry("700x400")
root.config(bg="white")
title = tk.Label(root, text="Typing Tutor", font=("Arial", 18, "bold"), bg="white")
title.pack(pady=10)
show_sentence = tk.Label(root, text=line, font=("Arial", 14), wraplength=600, bg="white")
show_sentence.pack(pady=15)
entry = tk.Entry(root, width=60, font=("Arial", 12))
entry.pack(pady=10)
btn1 = tk.Button(root, text="Start", command=start_typing, bg="green", fg="white")
btn1.pack(pady=5)
btn2 = tk.Button(root, text="Submit", command=check, bg="blue", fg="white")
btn2.pack(pady=5)
result = tk.Label(root, text="", font=("Arial", 12), bg="white")
result.pack(pady=15)
root.mainloop()