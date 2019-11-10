#!/usr/bin/env python3.6

from user import User

# creating a contact
def create_user(fname, lname, phone, email, password):
    '''
    creating a new user
    '''
    new_user = User(fname, lname, phone, email, password)
    return new_user

# save contact


def save_users(user):
    '''
    save new user
    '''
    user.save_user()

# delete contact
def del_user(user):
    '''
    delete a contact
    '''
    user.delete_user()

# find user
def find_user(first_name):
    '''
    find user using first name
    '''
    return User.find_by_first_name(first_name)

# if user exists
def check_existing_users(first_name):
    '''
    return a boolean if user exist
    '''
    return User.user_exist(first_name)

# display all contacts
def display_users():
    '''
    display all users
    '''
    return User.display_users()

################################################
    # *MAIN FUNCTION* #
################################################


def main():
    print("")
print(" ###################################\n      🤖**PASSWORD LOCKER**🤖\n ###################################\n\nPlease signup to continue\n")

print("Enter first name: ")
f_name = input()

print("Enter last name: ")
l_name = input()

print("Phone number: ")
p_number = input()

print("Email address: ")
e_address = input()

print("Enter password: ")
u_password = input()

# create and save new contact.
save_users(create_user(f_name, l_name, p_number, e_address, u_password))

print('\n')
print(f"Hi {f_name} {l_name}. Sign up was successful.🥳    😉 ")
print('\n')

while True:
    print(f"{f_name}, what would you like to do?")
    print('\n')
    print("Use these short codes : cc - create a new credential, dc - display credentials, fc - find a credential, ex - exit the user list ")

    short_code = input().lower()

    if short_code == 'cc':
        print("Please login first")

        print("\n")

        print("Enter your first name")
        search_first_name = input()
        if check_existing_users(search_first_name):
            search_user = find_user(search_first_name)

            print("Enter your first name")
            search_first_name = input()
            if check_existing_users(search_first_name):
                search_user = find_user(search_first_name)
            while True:
                print("Access granted")
                print("First name:-  ")
                f_name = input()

                print("Last name:-  ")
                l_name = input()

                print("Phone number:-  ")
                n_number = input()

                print("Email address:- ")
                e_address = input()

                print("create password:- ")
                p_password = input()

                # create new user and save the user
                save_users(create_user(f_name, l_name, n_number, e_address, p_password))

                print('\n')
                print(f"New user {f_name} {l_name} created")
                print('\n')

                break
            
        else:
            print("😡 User does not exist!! 🤬 ")
            print("Access denied"*100000000)

    # display user info
    elif short_code == 'dc':
        if display_users():
            print("Here's a list a list of all users 😇")
            print('\n')

            for user in display_users():
                print(
                    f"{user.first_name} {user.last_name} {user.phone_number} {user.email} {user.password}")
                print('\n')

        else:
            print('\n')
            print("No users to display 😶")
            print('\n')