# Mini Project 1: Attendance Tracker using Lists and Dictionaries
# USN: 25BTRAD039

students = {}  # {name: [total_classes, attended_classes]}

while True:
    print("\n1. Add Student")
    print("2. Mark Attendance")
    print("3. View Records & Percentages")
    print("4. Check Low Attendance Threshold")
    print("5. Exit")
    
    ch = input("Enter choice (1-5): ").strip()

    if ch == "1":
        name = input("Enter student name: ").strip()
        if name:
            students[name] = [0, 0]
            print(f"Student '{name}' added successfully.")
        else:
            print("Name cannot be empty.")

    elif ch == "2":
        name = input("Enter student name: ").strip()
        if name in students:
            status = input(f"Was {name} present? (y/n): ").strip().lower()
            students[name][0] += 1
            if status in ['y', 'yes', '1']:
                students[name][1] += 1
            print("Attendance updated.")
        else:
            print("Student not found! Please add the student first.")

    elif ch == "3":
        if not students:
            print("No student records available.")
        else:
            print("\n" + "=" * 50)
            print(f"{'Student Name':<15} | {'Total':<8} | {'Attended':<10} | {'Percentage'}")
            print("-" * 50)
            for name, (total, attended) in students.items():
                pct = (attended / total * 100) if total > 0 else 0.0
                print(f"{name:<15} | {total:<8} | {attended:<10} | {pct:.2f}%")
            print("=" * 50)

    elif ch == "4":
        try:
            limit = float(input("Enter minimum attendance percentage threshold (e.g., 75): "))
            print(f"\n--- Students below {limit}% ---")
            found = False
            for name, (total, attended) in students.items():
                pct = (attended / total * 100) if total > 0 else 0.0
                if pct < limit:
                    print(f"- {name}: {pct:.2f}% (Attended {attended}/{total})")
                    found = True
            if not found:
                print("All students meet or exceed the threshold.")
        except ValueError:
            print("Please enter a valid numeric threshold.")

    elif ch == "5":
        print("Exiting Attendance Tracker. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter a number between 1 and 5.")
