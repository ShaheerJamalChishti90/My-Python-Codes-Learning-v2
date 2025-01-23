import os
import csv
from datetime import datetime
import tkinter as tk
from tkinter import messagebox


def create_today_file():
    today = datetime.now()
    file_name = f"attendance_{today.strftime('%Y-%m-%d')}_{today.strftime('%A')}.csv"
    if not os.path.exists(file_name):
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Course", "Activity", "Arrival Time", "Departure Time", "Submission Timestamp"])
        return file_name, True
    return file_name, False  


def save_to_csv(name, course, activity, arrival, departure):
    today_file, _ = create_today_file()  
    timestamp = datetime.now().strftime('%Y-%m-%d %I:%M:%S-%p')  
    with open(today_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([name, course, activity, arrival, departure, timestamp])

# Function to handle the submission of data from the GUI
def submit_data():
    name = name_entry.get().strip()
    course = course_entry.get().strip()
    activity = activity_entry.get().strip()
    arrival = arrival_entry.get().strip()
    departure = departure_entry.get().strip()

    if not name or not course or not activity or not arrival or not departure:
        messagebox.showerror("Error", "All fields are required!")
        return

    save_to_csv(name, course, activity, arrival, departure)
    messagebox.showinfo("Success", "Attendance recorded successfully!")
    clear_fields()

# Function to clear the input fields
def clear_fields():
    name_entry.delete(0, tk.END)
    course_entry.delete(0, tk.END)
    activity_entry.delete(0, tk.END)
    arrival_entry.delete(0, tk.END)
    departure_entry.delete(0, tk.END)

# Create today's CSV file when the program starts
today_file, is_new = create_today_file()
if is_new:
    print(f"New file created: {today_file}")
else:
    print(f"File already exists: {today_file}")

# Set up the Tkinter window
root = tk.Tk()
root.title("KIT Attendance Application")
root.geometry("400x420")

# GUI Labels and Entry Fields
tk.Label(root, text="KIT ATTENDANCE FORM", font=("Arial", 20, "bold")).pack(pady=5)
tk.Label(root, text="Made by Shaheer Jamal", font=("Arial", 10, "bold")).pack(pady=0)

tk.Label(root, text="Name:", font=("Arial", 10, "bold")).pack(anchor='w', padx=20)
name_entry = tk.Entry(root, width=40)
name_entry.pack(padx=20, pady=5)

tk.Label(root, text="Course:", font=("Arial", 10, "bold")).pack(anchor='w', padx=20)
course_entry = tk.Entry(root, width=40)
course_entry.pack(padx=20, pady=5)

tk.Label(root, text="Activity:", font=("Arial", 10, "bold")).pack(anchor='w', padx=20)
activity_entry = tk.Entry(root, width=40)
activity_entry.pack(padx=20, pady=5)

tk.Label(root, text="When did you arrive? (HH:MM):", font=("Arial", 10, "bold")).pack(anchor='w', padx=20)
arrival_entry = tk.Entry(root, width=40)
arrival_entry.pack(padx=20, pady=10)

tk.Label(root, text="When did you leave? (HH:MM):", font=("Arial", 10, "bold")).pack(anchor='w', padx=20)
departure_entry = tk.Entry(root, width=40)
departure_entry.pack(padx=20, pady=10)

# Submit Button
submit_button = tk.Button(root, text="SUBMIT", font=("Arial", 15, "bold"), command=submit_data, bg="green", fg="white")
submit_button.pack(padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()
