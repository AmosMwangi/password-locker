import unittest
import pyperclip
from credential import Credential


class TestCredential(unittest.TestCase):
    '''
    This test defines credential class behavior
    '''
# => 1
    '''
    test 1 : check if it's been instatiated correctly
    '''

    def setUp(self):
        self.new_credential = Credential(
            "Moringa", "School", "0712345678", "ms@mail.com", "password")

    def test_init(self):
        self.assertEqual(self.new_credential.first_name, "Moringa")
        self.assertEqual(self.new_credential.last_name, "School")
        self.assertEqual(self.new_credential.phone_number, "0712345678")
        self.assertEqual(self.new_credential.email, "ms@mail.com")
        self.assertEqual(self.new_credential.password, "password")

# => 2
    '''
    test 2 : test if a new credential can be added
    '''

    def test_save_credential(self):
        self.new_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 1)

# => 3
    '''
    test 3 : Use teardown method which helps in cleaning up code
    '''

    def tearDown(self):
        Credential.credential_list = []
##
    '''
    test for saving multi-credentials
    '''

    def test_save_multiple_credential(self):
        self.new_credential.save_credential()
        test_credential = Credential(
            "Moringa", "School", "0712345678", "ms@mail.com", "password")
        test_credential.save_credential()
        self.assertEqual(len(Credential.credential_list), 2)

# => 4
    '''
    test 4 : Deleting a credential
    '''

    def test_delete_credential(self):
        self.new_credential.save_credential()
        test_credential = Credential(
            "Moringa", "School", "0712345678", "ms@mail.com", "password")
        test_credential.save_credential()
        self.new_credential.delete_credential()
        self.assertEqual(len(Credential.credential_list), 1)

# => 5
    '''
    test 5 : find credential by first name and display info
    '''

    def test_find_credential_by_first_name(self):
        self.new_credential.save_credential()
        test_credential = Credential(
            "Moringa", "School", "0712345678", "ms@mail.com", "password")
        test_credential.save_credential()
        found_credential = Credential.find_by_first_name("Moringa")
        self.assertEqual(found_credential.email, test_credential.email)


# => 6
    '''
    test 6 : if a credential exists return a boolean
    '''

    def test_credential_exists(self):
        self.new_credential.save_credential()
        test_credential = Credential(
            "Moringa", "School", "0712345678", "ms@mail.com", "password")
        test_credential.save_credential()
        credential_exists = Credential.credential_exist("Moringa")
        self.assertTrue(credential_exists)

# => 7
    '''
    test 7 : display list of all credentials saved
    '''

    def test_display_all_credentials(self):
        self.assertEqual(Credential.display_credentials(),
                         Credential.credential_list)

# => 8
    '''
    test 8 : copy using pyperclip
    '''

    # def test_copy_email(self):
    #     self.new_user.save_user()
    #     User.copy_email("0712345678")

    #     self.assertEqual(self.new_user.email, pyperclip.paste())


if __name__ == '__main__':
    unittest.main()
