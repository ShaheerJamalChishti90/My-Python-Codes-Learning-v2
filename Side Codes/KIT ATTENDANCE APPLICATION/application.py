import os
import csv
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

# Function to create today's CSV file if it doesn't exist
def create_today_file():
    today = datetime.now()
    file_name = f"attendance_{today.strftime('%Y-%m-%d')}_{today.strftime('%A')}.csv"
    if not os.path.exists(file_name):
        with open(file_name, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Course", "Activity", "Arrival Time", "Departure Time", "Submission Timestamp"])
        return file_name, True  # File created
    return file_name, False  # File already exists

# Function to save student details into the CSV file
def save_to_csv(name, course, activity, arrival, departure):
    today_file, _ = create_today_file()  # Ensure today's file exists
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Submission timestamp
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
root.title("Attendance Application")
root.geometry("400x400")

# GUI Labels and Entry Fields
tk.Label(root, text="Attendance Form", font=("Arial", 16, "bold")).pack(pady=10)

tk.Label(root, text="Name:").pack(anchor='w', padx=20)
name_entry = tk.Entry(root, width=30)
name_entry.pack(padx=20, pady=5)

tk.Label(root, text="Course:").pack(anchor='w', padx=20)
course_entry = tk.Entry(root, width=30)
course_entry.pack(padx=20, pady=5)

tk.Label(root, text="Activity:").pack(anchor='w', padx=20)
activity_entry = tk.Entry(root, width=30)
activity_entry.pack(padx=20, pady=5)

tk.Label(root, text="Arrival Time (HH:MM):").pack(anchor='w', padx=20)
arrival_entry = tk.Entry(root, width=30)
arrival_entry.pack(padx=20, pady=5)

tk.Label(root, text="Departure Time (HH:MM):").pack(anchor='w', padx=20)
departure_entry = tk.Entry(root, width=30)
departure_entry.pack(padx=20, pady=5)

# Submit Button
submit_button = tk.Button(root, text="Submit", command=submit_data, bg="green", fg="white")
submit_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
