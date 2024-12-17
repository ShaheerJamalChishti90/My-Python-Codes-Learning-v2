import datetime

attendance_data = {}

def attedance_record():
    name = input("Enter your name: ").capitalize()
    activity = input("Enter what you did today: ").capitalize()
    date = datetime.date.today()

    attendance_data[name] = {
        "activity": activity,
        "date": date    
    }
    print("Your attendance is recorded successfully!")

    
def display_attendace_date():
    print("\nAttendance Summary:")
    
    # Get all items from the attendance_data dictionary
    attendance_items = attendance_data.items()
    
    # Loop through each item in the attendance_items
    for item in attendance_items:
        # Each item is a tuple containing the name and the info dictionary
        name = item[0]  # The first element is the name
        info = item[1]  # The second element is the info dictionary
        
        # Extract activity and timestamp from the info dictionary
        activity = info['activity']
        date = info['date']
        
        # Print the attendance record
        print(f"Name: {name}, Activity: {activity}, Time: {date}")

def main():
    while True:
        print("\nAttendance Application")
        print("1. Record Attendance")
        print("2. Display Attendance")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            attedance_record()
        elif choice == '2':
            display_attendace_date()
        elif choice == '3':
            print("Exiting the application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()