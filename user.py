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

    @classmethod
    def find_by_first_name(cls, first_name):
        '''
        search name & return detail info
        '''
        for user in cls.user_list:
            if user.first_name == first_name:
                return user
    
    @classmethod
    def user_exist(cls, first_name):
        '''
        checks if a user exists
        '''
        for user in cls.user_list:
            if user.first_name == first_name:
                return True
        else:
            return False
        
    @classmethod
    def display_users(cls):
        '''
        return user list
        '''
        return cls.user_list

    @classmethod
    def copy_email(cls, first_name):
        user_found = User.find_by_first_name(first_name)
        pyperclip.copy(user_found.email)