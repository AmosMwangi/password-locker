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
