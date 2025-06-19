from os import name
#step1  Initialize an empty contact book
contacts={}
#step2 Display the menu
def show_menu():
    print("---Contact book menu---")
    print("1. Add Contact")
    print("2. View Contact")
    print("3. Search Contact")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. Exit")

#step 3  Add a contact
def add_contact():
    name=input("Enter contact name:")
    phone=input("Enter contact number: ")
    email=input("Enter email: ")
    contacts[name]= {"phone":phone, "email":email}
    print(f"Contact {name} has been added to your contact book successfully! ")
#step 4 View All Contacts
def view_contact():
    if contacts:
        print("\n---Contact List---")
        for name, details in contacts.items():
            print(f"Name:{name}")
            print(f"Phone: {details['phone']}")
            print(f"Email: {details['email']}")
    else:
        print("Your contact book is empty.")

#Step5 Search a contact   
def search_contact():
    name= input("Enter the name of the contact you want to search:")
    if name in contacts:
        print(f"\n ---Contact Details for {name}---")
        print(f"Name: {name}")
        print(f"Phone:{contacts[name] ['phone']}") 
        print(f"Email:{contacts[name] ['email']}")
    else:
        print(f"Contact {name} not found in your contact book.")

#step6 Edit a contact 
def edit_contact():
    name = input("Enter the name of the contact you want to edit:")
    if name in contacts:
        phone= input("Enter new phone number:")
        email= input("Enter new email:")
        contacts[name]={"Phone":phone, "email":email}
        print(f"Contact {name} has been updated successfully!")
    else:
        print(f"Contact {name} not found in your contact book.")

#step7 Delete a contact
def delete_contact():
    name = input("Enter the name of the contact you want to delete:")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} has been deleted successfully!")
    else:
        print(f"Contact {name} not found in your contact book.")

 #step8 main program loop
while True:
    show_menu()
    choice = input("Enter your choice (1-6):")

    if choice=="1":
        add_contact()
    elif choice=="2":
        view_contact()
    elif choice=="3":
        search_contact()
    elif choice=="4":
        edit_contact()
    elif choice=="5":
        delete_contact()
    elif choice=="6":
        print("Thank you for using the Contact Book, Goodbye!")
        break
    else:
        print("Invalid choice, Please select a valid option(1-6).")    








      
