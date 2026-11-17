# Lab Exercise 16: Dice Simulator using random module
import random

while True:
    print("\n1. Roll One Die")
    print("2. Roll Two Dice")
    print("3. Roll One Die Many Times (frequency)")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        result = random.randint(1, 6)
        print("Dice result:", result)
    elif choice == "2":
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        print("First die:", die1)
        print("Second die:", die2)
        print("Total:", die1 + die2)
    elif choice == "3":
        n = int(input("Enter number of rolls: "))
        frequency = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
        for i in range(n):
            frequency[random.randint(1, 6)] += 1
        print("\nFace  Count  Percent  Bar")
        for face, count in frequency.items():
            percent = count / n * 100
            print("{:<6}{:<7}{:>6.1f}%  {}".format(face, count, percent, "*" * round(percent)))
    elif choice == "4":
        print("Dice simulation ended.")
        break
    else:
        print("Invalid choice.")
