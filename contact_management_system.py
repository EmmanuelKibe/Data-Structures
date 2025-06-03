#Initialize an empty dictionary to store contacts
contact_list = {}	

def create_contact():
    name = input("Enter the name of the contact: ")
    number_and_email = input("Enter the phone number and email of the contact separated by a comma: ")
    number_and_email = ((int(number), email).strip() for number, email in number_and_email.split(', ')) 
    contact_list[name] = number_and_email
    print(f"Contact {name} created successfully!")
    

create_contact()
