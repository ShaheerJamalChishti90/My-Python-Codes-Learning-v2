import datetime

# Dictionary to store attendance data
attendance_data = {}

def record_attendance():
    name = input("Enter your name: ")
    activity = input("Enter what you did: ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Record the attendance
    attendance_data[name] = {
        "activity": activity,
        "timestamp": timestamp
    }
    print("Attendance recorded successfully!")

def display_attendance():
    print("\nAttendance Summary:")
    for name, info in attendance_data.items():
        print(f"Name: {name}, Activity: {info['activity']}, Time: {info['timestamp']}")

def main():
    while True:
        print("\nAttendance Application")
        print("1. Record Attendance")
        print("2. Display Attendance")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            record_attendance()
        elif choice == '2':
            display_attendance()
        elif choice == '3':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()