# Lab Exercise 8: Contact Book using Lists and Dictionaries
contacts = []  # list of dictionaries


def find_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            return contact
    return None


def add_contact():
    name = input("Enter name: ")
    if find_contact(name):
        print("Contact already exists!")
        return
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    print("Contact added successfully!")


def search_contact():
    name = input("Enter name to search: ")
    contact = find_contact(name)
    if contact:
        print("Name:", contact["name"])
        print("Phone:", contact["phone"])
        print("Email:", contact["email"])
    else:
        print("Contact not found!")


def update_contact():
    name = input("Enter name to update: ")
    contact = find_contact(name)
    if contact:
        contact["phone"] = input("Enter new phone number: ")
        contact["email"] = input("Enter new email: ")
        print("Contact updated successfully!")
    else:
        print("Contact not found!")


def delete_contact():
    name = input("Enter name to delete: ")
    contact = find_contact(name)
    if contact:
        contacts.remove(contact)
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")


def display_contacts():
    if not contacts:
        print("No contacts available!")
    else:
        print("\nName\t\tPhone\t\tEmail")
        print("-" * 50)
        for contact in contacts:
            print(contact["name"] + "\t\t" + contact["phone"] + "\t" + contact["email"])


while True:
    print("\n--- CONTACT BOOK ---")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display Contacts")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        update_contact()
    elif choice == "4":
        delete_contact()
    elif choice == "5":
        display_contacts()
    elif choice == "6":
        print("Exiting Contact Book.")
        break
    else:
        print("Invalid choice!")
