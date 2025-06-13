#store website log in details in a dictionary
login_info = {'instagram.com': ('ManuIceman', 'justerini123'), 'ecitizen.com': ('Emmanuel Kibe', 'gov@1'), 'spotify.com': ('ManuIceman', 'Music@12')}

#update login information    
def update_info(website):
    if website not in login_info:
        print("Information on the website does not exist")
    else:
        choice = int(input('What would you like to change:\n1) Username\n2) Password'))
        if choice == 1:
            while True:
                current_username = input("Enter your current username: ")
                
                if current_username != login_info[website][0]:
                    print("Wrong username. Try again")
                else:
                    print("Good!")
                    new_username = input("Enter your new username: ")
                    if new_username == login_info[website][0]:
                        print("New username cannot be your old username!")
                    else:
                        login_info[website] = (new_username, login_info[website][1])
                        print(f"You have successfully updated your username for {website}:\nNew username - {new_username}")
                        break
                    
        elif choice == 2:
            while True:
                current_password = input("Enter your current password: ")
                
                if current_password != login_info[website][1]:
                    print("Wrong password. Try again")
                else:
                    print("Good!")
                    new_password = input("Enter your new password: ")
                    if new_password == login_info[website][1]:
                        print("New password cannot be your old password!")
                    else:
                        login_info[website] = (login_info[website][0], new_password)
                        print(f"You have successfully updated your password for {website}:\nNew password - {new_password}")
                        break
                    
        else:
            print("Input a valid choice!")
            
#add new login information
def add_info():
    new_website = input("Enter the name of the website you want to add: ")
    if new_website in login_info:
        choice = int(input("Information on this website already exists. Would you like to update it instead:\n1) Update information\n2) Exit\n"))
        
        if choice == 1:
            update_info(new_website)
        elif choice == 2:
            print("Exiting...")
        else:
            print("Input a valid choice!")
        
    else:
        username = input("Enter your preferred username: ")
        password = input("Choose a strong password: ")
        login_info[new_website] = (username, password)
        
        print(f"You have successfuly added information on {new_website}:\nUsername - {username}\nPassword - {password}")

#retrieve information on a certain website
def retrieve_info(website):
    if website not in login_info:
        print("Information on the website does not exist")
    else:
        print(f"{website} -> Username: {login_info[website][0]}, Password: {login_info[website][1]}")

#delete information about a website
def delete_info(website):
    if website not in login_info:
        print("Information on the website does not exist")
    else:
       del login_info[website]
       print(f"Succesfully deleted '{website}' information")