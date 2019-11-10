import unittest
import pyperclip
from user import User

class TestUser(unittest.TestCase):
    '''
    This test defines user class behavior
    '''
# => 1
    '''
    test 1 : check if it's been instatiated correctly
    '''

    def setUp(self):
        self.new_user = User("Moringa", "School", "0712345678", "ms@mail.com", "password")
    
    
