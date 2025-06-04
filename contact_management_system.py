#Initialize an empty dictionary to store contacts
contact_list = {}	

caller1 = {'Gabriel Oguda' : ('0799617083', 'oguda@gmail.com')}
contact_list.update(caller1)
# Add a new contact
def create_contact():
    name = input("Enter the name of the contact: ")
    number_and_email = input("Enter the phone number and email of the contact separated by a comma: ")
    number, email = number_and_email.split(',')
    number = number.strip()
    email = email.strip()
    contact_list[name] = (number, email)
    print(f"Contact {name} created successfully!")

#delete a contact    
def delete_contact(number):
    if number in contact_list:
        del contact_list[number]
        print(f"Contact {number} deleted successfully!")
    else:
        print(f"Contact {number} not found.")

def search_contact():
    search_method = input("How would you like to search for the contact (type '1' for name and '2' for number): ")
    match search_method.strip():
        case '1':
            name = input("Enter the name of the contact: ")
            if name in contact_list:
                print(f"{name} : {contact_list[name]}")
                print("Search successful!")
            else:
                print("Contact not found")
        
        case '2':
            number = input("Input the mobile number: ").strip()
            found = False
            for name, (num, email) in contact_list.items():
                if number == num:
                    print(f"Contact found: {name} : ({num}, {email})")
                    found = True
                    break
            if not found:
                print("Contact not found")
                
        case _:
            print("Error! Input a valid option")
            
#list all contacts
def list_contacts():
    if contact_list:
        print("List of contacts:")
        for name, (number, email) in contact_list.items():
            print(f"{name} : ({number}, {email})")
    else:
        print("No contacts found.")

list_contacts()

