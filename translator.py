attendance_record = {}

def mark_attendance():
    print("Enter attendance (type 'exit' to quit):")
    while True:
        name = input("Enter name: ").strip()
        if name.lower() == 'exit':
            print("Exiting attendance system...")
            break
        
        status = input("Enter status (Present/Absent): ").strip().capitalize()
        if status not in ['Present', 'Absent']:
            print("Invalid status! Please enter 'Present' or 'Absent'.")
            continue

        attendance_record[name] = status
        print("\nCurrent Attendance:")
        for person, stat in attendance_record.items():
            print(f"{person}: {stat}")
        print()

mark_attendance()






