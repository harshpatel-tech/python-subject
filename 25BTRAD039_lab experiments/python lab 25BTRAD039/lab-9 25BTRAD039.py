# Lab Exercise 9: Student Grading System
students = {}  # dictionary: name -> marks


def calculate_grade(marks):
    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


n = int(input("Enter number of students: "))
for i in range(n):
    name = input("\nEnter student name: ")
    marks = float(input("Enter marks out of 100: "))
    if marks < 0 or marks > 100:
        print("Invalid marks! Enter marks between 0 and 100.")
        continue
    students[name] = marks

print("\n--- STUDENT RESULTS ---")
for name, marks in students.items():
    print("Name:", name)
    print("Marks:", marks)
    print("Grade:", calculate_grade(marks))
    print("-" * 20)

if students:
    average = sum(students.values()) / len(students)
    topper = max(students, key=students.get)
    print("Class Average:", round(average, 2))
    print("Topper:", topper, "with", students[topper], "marks")
