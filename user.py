import pyperclip

class User:
    '''
    user class
    '''

    user_list = []

    def __init__(self, first_name, last_name, number, email, password):

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email
        self.password = password

    def save_user(self):
        '''
        saves users into user_list
        '''
        User.user_list.append(self)
    
    def delete_user(self):
        '''
        delete's a saved user from user_list
        '''
        User.user_list.remove(self)