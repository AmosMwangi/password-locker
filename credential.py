import pyperclip


class Credential:
    '''
    Credentials class
    '''
    credential_list = []

    def __init__(self, first_name, last_name, number, email, password):

        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = number
        self.email = email
        self.password = password

    def save_credential(self):
        '''
        saves Credentials into Credential_list
        '''
        Credential.credential_list.append(self)

    def delete_credential(self):
        '''
        delete's a saved user from user_list
        '''
        Credential.credential_list.remove(self)

    @classmethod
    def find_by_first_name(cls, first_name):
        '''
        search name & return detail info
        '''
        for credential in cls.credential_list:
            if credential.first_name == first_name:
                return credential

    @classmethod
    def credential_exist(cls, first_name):
        '''
        checks if a Credential exists
        '''
        for credential in cls.credential_list:
            if credential.first_name == first_name:
                return True
        else:
            return False

    @classmethod
    def display_credentials(cls):
        '''
        return credential list
        '''
        return cls.credential_list

    @classmethod
    def copy_email(cls, first_name):
        credential_found = Credential.find_by_first_name(first_name)
        pyperclip.copy(credential_found.email)
