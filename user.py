import pyperclip

class User:
    '''
    user class
    '''

    user_list = []

    def __init__(self, user_name, password):

        self.user_name = user_name
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
    def find_by_user_name(cls, user_name):
        '''
        search name & return detail info
        '''
        for user in cls.user_list:
            if user.user_name == user_name:
                return user
    
    @classmethod
    def user_exist(cls, user_name):
        '''
        checks if a user exists
        '''
        for user in cls.user_list:
            if user.user_name == user_name:
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
    def copy_email(cls, user_name):
        user_found = User.find_by_user_name(user_name)
        pyperclip.copy(user_found.email)
    
