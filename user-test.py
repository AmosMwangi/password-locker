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
    
# => 2
    '''
    test 2 : test if a new user can be added
    '''

    def test_save_user(self):
        self.new_user.save_user()
        self.assertEqual(len(User.user_list), 1)

# => 3
    '''
    test 3 : Use teardown method which helps in cleaning up code
    '''

    def tearDown(self):
        User.user_list = []
##
    '''
    test for saving multi-users
    '''

    def test_save_multiple_user(self):
        self.new_user.save_user()
        test_user = User("Moringa", "School", "0712345678", "ms@mail.com", "password")
        test_user.save_user()
        self.assertEqual(len(User.user_list), 2)

# => 4
    '''
    test 4 : Deleting a user
    '''

    def test_delete_user(self):
        self.new_user.save_user()
        test_user = User("Moringa", "School", "0712345678", "ms@mail.com", "password")
        test_user.save_user()
        self.new_user.delete_user()
        self.assertEqual(len(User.user_list), 1)

