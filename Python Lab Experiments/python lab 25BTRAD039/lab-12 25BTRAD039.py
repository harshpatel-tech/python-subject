# Lab Exercise 12: Student Data Manager using Files
import os

filename = "students.txt"


def read_records():
    if not os.path.exists(filename):
        return []
    with open(filename, "r") as file:
        return [line.strip() for line in file if line.strip()]


def display_students():
    records = read_records()
    if not records:
        print("No student records found.")
        return
    print("Roll No | Name | Marks")
    print("-" * 25)
    for record in records:
        roll, name, marks = record.split(",")
        print(roll, "|", name, "|", marks)


def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter student name: ")
    marks = input("Enter marks: ")
    if not roll.isdigit() or not marks.isdigit():
        print("Roll number and marks must be numeric.")
        return
    if not name.strip() or int(marks) > 100:
        print("Invalid name or marks (marks must be 0-100).")
        return
    for record in read_records():
        if record.split(",")[0] == roll:
            print("Roll number already exists.")
            return
    with open(filename, "a") as file:
        file.write(roll + "," + name + "," + marks + "\n")
    print("Student added successfully.")


def search_student():
    roll = input("Enter roll number to search: ")
    for record in read_records():
        data = record.split(",")
        if data[0] == roll:
            print("Roll No:", data[0])
            print("Name :", data[1])
            print("Marks:", data[2])
            return
    print("Student not found.")


def update_student():
    roll = input("Enter roll number to update: ")
    records = read_records()
    found = False
    for i in range(len(records)):
        data = records[i].split(",")
        if data[0] == roll:
            name = input("Enter new name: ")
            marks = input("Enter new marks: ")
            if not name.strip() or not marks.isdigit() or int(marks) > 100:
                print("Invalid input.")
                return
            records[i] = roll + "," + name + "," + marks
            found = True
            break
    if found:
        with open(filename, "w") as file:
            for record in records:
                file.write(record + "\n")
        print("Student updated successfully.")
    else:
        print("Student not found.")


while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_student()
    elif choice == "2":
        display_students()
    elif choice == "3":
        search_student()
    elif choice == "4":
        update_student()
    elif choice == "5":
        print("Exiting program.")
        break
    else:
        print("Invalid choice.")
