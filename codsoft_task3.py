contacts = {}  # We define a Dictionary to store contacts (name: phone_number)

# Function to add a contact
def add_contact(name, phone_number):
    if name not in contacts:
        contacts[name] = phone_number
        print(f"Contact '{name}' with phone number '{phone_number}' has been added.")
    else:
        print(f"Contact '{name}' already exists in the contact book.")

# Function to view all the contacts
def view_contacts():
    if not contacts:
        print("Your contact book is empty.")
    else:
        print("Contacts:")
        for name, phone_number in contacts.items():
            print(f"{name}: {phone_number}")

# Function to search for a contact
def search_contact(name):
    if name in contacts:
        print(f"Contact '{name}': {contacts[name]}")
    else:
        print(f"Contact '{name}' not found in the contact book.")

# Main Program Loop
while True:
    print("\nOptions:")
    print("1. Add a contact")
    print("2. View all contacts")
    print("3. Search for a contact")
    print("4. Quit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        name = input("Enter the contact name: ")
        phone_number = input("Enter the phone number: ")
        add_contact(name, phone_number)
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        name = input("Enter the contact name to search: ")
        search_contact(name)
    elif choice == '4':
        print("Goodbye, have a nice day!")
        break
    else:
        print("Invalid choice. Please try again.")

