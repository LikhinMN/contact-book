import json
import os

FILENAME = "contacts.json"

def load_contacts():
    global contacts
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            contacts = json.load(file)
    else:
        contacts = []

def save_contacts():
    with open(FILENAME, "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(name, phone, email, address):
    sample = {"name": name, "details": {"phone": phone, "email": email, "address": address}}
    contacts.append(sample)
    save_contacts()  # Save after each modification

def view_contacts():
    if not contacts:
        print("No contacts to show.")
    else:
        for index, contact in enumerate(contacts, start=1):
            print(f"\nContact {index}")
            print(f"Name   : {contact['name']}")
            print(f"Phone  : {contact['details']['phone']}")
            print(f"Email  : {contact['details']['email']}")
            print(f"Address: {contact['details']['address']}")

def search_contact(name):
    found = False
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print(f"\nName   : {contact['name']}")
            print(f"Phone  : {contact['details']['phone']}")
            print(f"Email  : {contact['details']['email']}")
            print(f"Address: {contact['details']['address']}")
            found = True
            break
    if not found:
        print("Contact not found.")

def update_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            print("What do you want to update? (phone/email/address)")
            field = input("Enter field: ").strip().lower()
            if field in contact["details"]:
                new_value = input(f"Enter new {field}: ").strip()
                contact["details"][field] = new_value
                save_contacts()  # Save after modification
                print(f"{field} updated successfully!")
            else:
                print("Invalid field.")
            return
    print("Contact not found.")

def delete_contact(name):
    for contact in contacts:
        if contact["name"].lower() == name.lower():
            contacts.remove(contact)
            save_contacts()  # Save after deletion
            print(f"Contact '{name}' deleted.")
            return
    print("Contact not found.")

load_contacts()  # Ensure contacts are loaded before use

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contacts")
    print("4. Update Contacts")
    print("5. Delete Contacts")
    print("6. Exit")
    choice = input("Enter your choice: ").strip()

    if choice == "1":
        name = input("Enter name: ").strip()
        phone = input("Enter phone: ").strip()
        email = input("Enter email: ").strip()
        address = input("Enter address: ").strip()
        add_contact(name, phone, email, address)
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search = input("Enter the name to search: ").strip()
        search_contact(search)
    elif choice == "4":
        update = input("Enter the name to update: ").strip()
        update_contact(update)
    elif choice == "5":
        delete = input("Enter the name to delete: ").strip()
        delete_contact(delete)
    elif choice == "6":
        save_contacts()
        print("Contacts saved. Exiting...")
        break
    else:
        print("Invalid choice.")