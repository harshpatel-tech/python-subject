# Lab Exercise 15: Library Management System (with inheritance)
class Item:  # base class
    def __init__(self, title):
        self.title = title
        self.available = True

    def issue(self):
        if self.available:
            self.available = False
            print("Book issued successfully.")
        else:
            print("Book is already issued.")

    def give_back(self):
        if not self.available:
            self.available = True
            print("Book returned successfully.")
        else:
            print("Book was not issued.")


class Book(Item):  # derived class
    def __init__(self, title, author):
        super().__init__(title)
        self.author = author

    def display(self):
        status = "Available" if self.available else "Issued"
        print(self.title, "-", self.author, "-", status)


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print("Book added successfully.")

    def find_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def display_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                book.display()

    def issue_book(self, title):
        book = self.find_book(title)
        if book:
            book.issue()
        else:
            print("Book not found.")

    def return_book(self, title):
        book = self.find_book(title)
        if book:
            book.give_back()
        else:
            print("Book not found.")


library = Library()
library.add_book(Book("Python Basics", "John"))
library.add_book(Book("Java Programming", "James"))
library.add_book(Book("Data Structures", "Alice"))

while True:
    print("\n1. Display Books")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Add Book")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        library.display_books()
    elif choice == "2":
        library.issue_book(input("Enter book title: "))
    elif choice == "3":
        library.return_book(input("Enter book title: "))
    elif choice == "4":
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        library.add_book(Book(title, author))
    elif choice == "5":
        print("Exiting library system.")
        break
    else:
        print("Invalid choice.")
