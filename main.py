#!/usr/bin/env python3.6

import random

from user import User

from credential import Credential

# creating a contact
def create_user(fname, password):
    '''
    creating a new user
    '''
    new_user = User(fname, password)
    return new_user

# creating a credential
def create_credential(fname, lname, phone, email, password):
    '''
    creating a new user
    '''
    new_credential = Credential(fname, lname, phone, email, password)
    return new_credential

# save contact

def save_users(user):
    '''
    save new user
    '''
    user.save_user()

# save credential
def save_credentials(user):
    '''
    save new user
    '''
    user.save_credential()

# delete contact
def del_user(user):
    '''
    delete a contact
    '''
    user.delete_user()

# delete credential
def del_user(user):
    '''
    delete a contact
    '''
    user.delete_user()

# find user
def find_user(user_name):
    '''
    find user using user name
    '''
    return User.find_by_user_name(user_name)


# if user exists
def check_existing_users(first_name):
    '''
    return a boolean if user exist
    '''
    return User.user_exist(first_name)

# display all contacts
def display_credentials():
    '''
    display all users
    '''
    return Credential.display_credentials()

# delete credential
def del_credentials(password):
    '''
    function for deleting a credential
    '''
    found_credential = Credential.find_by_password(password)
    Credential.delete_credential(found_credential)

################################################
    # *MAIN FUNCTION* #
################################################


def main():
    print("")
print(" ###################################\n      🤖**PASSWORD LOCKER**🤖\n ###################################\n\nPlease signup to continue\n")

print("Enter user name: ")
f_name = input()

print("Enter password: ")
u_password = input()

# create and save new contact.
save_users(create_user(f_name, u_password))

print('\n')
print(f"Hi {f_name}. Sign up was successful.🥳   😉 ")
print('\n')

while True:
    print(f"{f_name}, what would you like to do?")
    print('\n')
    print("Use these short codes : cc - create a new credential, dc - display credentials, fc - find a credential, dc - delete credential ex - exit the user list ")

    short_code = input().lower()

    if short_code == 'cc':
        print("Please login first")

        print("\n")

        print("Enter your user name")
        search_user_name = input()
        if check_existing_users(search_user_name):
            search_user = find_user(search_user_name)
            while True:
                print('-' * 14)
                print('-' * 14)
                print("Access granted")
                print('-' * 14)
                print('-' * 14)
                print("First name:-  ")
                fi_name = input()

                print("Last name:-  ")
                li_name = input()

                print("Phone number:-  ")
                ni_number = input()

                print("Email address:- ")
                ei_address = input()

                print("Select Y to create your own password")
                response = input().lower()

                if response == 'y':
                    print('password ....')
                    pi_password = input().lower()

                else:
                    x = []
                    r = range(306, 399)
                    for n in r:
                        x.append(str(n))
                    pi_password = (fi_name+li_name+random.choice(x))
                    print(f"Your password is ...{pi_password}")

                # create new user and save the user
                save_credentials(create_credential(fi_name, li_name, ni_number, ei_address, pi_password))

                print('\n')
                print(f"New credential {fi_name} created")
                print('\n')

                break
            
        else:
            print("😡 user does not exist!! 🤬 ")
            print("Access denied"*100000000)

    # display user info
    elif short_code == 'dc':
        if display_credentials():
            print("Here's a list a list of all users 😇")
            print('\n')

            for credential in display_credentials():
                print(
                    f"{credential.first_name} {credential.last_name} {credential.phone_number} {credential.email} {credential.password}")
                print('\n')

        else:
            print('\n')
            print("No credentials to display 😶")
            print('\n')

        # find credential
    elif short_code == 'fc':
        print("Spin search loaded \nEnter first name: ")

        search_first_name = input()
        if check_existing_users(search_first_name):
            search_credential = find_credential(search_first_name)
            print(f"{search_credential.first_name} {search_credential.last_name} ")

            print('-' * 20)

            print(f"Phone number...{search_credential.phone_number}")

            print(f"Email address...{search_credential.email}")

            print(f"Password....{search_credential.password}")

        else:
            print("User does not exist!! 🥵")
        
    elif short_code == 'dc':
        print("First enter your password: ")
        password = input()

    elif short_code == "ex":
        print(f"Bye, {f_name}. Have a lovely time 🤗  .")
        break
    else:
        print(f"Sorry {f_name} I really didn't get that request 😵. Please use the clear short code 🧐")


if __name__ == '__main__':

    main()