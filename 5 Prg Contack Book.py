contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
    print("✅ Contact added.")

def view_contacts():
    if not contacts:
        print("📭 No contacts found.")
    for name, details in contacts.items():
        print(f"\n👤 {name}")
        for key, value in details.items():
            print(f"   {key}: {value}")

def search_contact():
    name = input("🔎 Enter name to search: ")
    if name in contacts:
        print(f"\n👤 {name}")
        for key, value in contacts[name].items():
            print(f"   {key}: {value}")
    else:
        print("❌ Contact not found.")

def update_contact():
    name = input("✏️ Enter contact name to update: ")
    if name in contacts:
        phone = input("New phone: ")
        email = input("New email: ")
        address = input("New address: ")
        contacts[name] = {'Phone': phone, 'Email': email, 'Address': address}
        print("🔄 Contact updated.")
    else:
        print("❌ Contact not found.")

def delete_contact():
    name = input("🗑️ Enter contact name to delete: ")
    if name in contacts:
        del contacts[name]
        print("🧹 Contact deleted.")
    else:
        print("❌ Contact not found.")

def menu():
    while True:
        print("\n==== 📒 CONTACT BOOK MENU ====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("👉 Enter your choice (1-6): ")

        if choice == '1': add_contact()
        elif choice == '2': view_contacts()
        elif choice == '3': search_contact()
        elif choice == '4': update_contact()
        elif choice == '5': delete_contact()
        elif choice == '6': print("👋 Exiting..."); break
        else: print("❗ Invalid choice. Try again.")

menu()
