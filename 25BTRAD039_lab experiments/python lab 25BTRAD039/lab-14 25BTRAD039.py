# Lab Exercise 14: Bank Account System using OOP
class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance  # private attribute (encapsulation)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print("Withdrawal successful.")

    def check_balance(self):
        print("Account Holder:", self.name)
        print("Current Balance: Rs.", self.__balance)


account = BankAccount("Harsh", 5000)
while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        try:
            amount = float(input("Enter deposit amount: "))
            account.deposit(amount)
        except ValueError:
            print("Please enter a valid number.")
    elif choice == "2":
        try:
            amount = float(input("Enter withdrawal amount: "))
            account.withdraw(amount)
        except ValueError:
            print("Please enter a valid number.")
    elif choice == "3":
        account.check_balance()
    elif choice == "4":
        print("Thank you for using the bank system.")
        break
    else:
        print("Invalid choice.")
