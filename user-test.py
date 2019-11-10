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
    
    def test_init(self):
        self.assertEqual(self.new_user.first_name, "Moringa")
        self.assertEqual(self.new_user.last_name, "School")
        self.assertEqual(self.new_user.phone_number, "0712345678")
        self.assertEqual(self.new_user.email, "ms@mail.com")
        self.assertEqual(self.new_user.password, "password")

