class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}"


class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone, email):
        contact = Contact(name, phone, email)
        self.contacts.append(contact)
        print(f"Contact '{name}' added.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        for contact in self.contacts:
            print(contact)

    def search_contact(self, name):
        found_contacts = [contact for contact in self.contacts if name.lower() in contact.name.lower()]
        if not found_contacts:
            print(f"No contacts found with the name '{name}'.")
            return
        for contact in found_contacts:
            print(contact)

    def delete_contact(self, name):
        initial_count = len(self.contacts)
        self.contacts = [contact for contact in self.contacts if name.lower() not in contact.name.lower()]
        if len(self.contacts) < initial_count:
            print(f"Contact(s) with the name '{name}' deleted.")
        else:
            print(f"No contact found with the name '{name}'.")


def display_menu():
    print("\nContact Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")


def main():
    manager = ContactManager()

    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter contact phone: ")
            email = input("Enter contact email: ")
            manager.add_contact(name, phone, email)
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            name = input("Enter name to search: ")
            manager.search_contact(name)
        elif choice == '4':
            name = input("Enter name to delete: ")
            manager.delete_contact(name)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
