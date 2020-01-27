import unittest

from user import User

class TestUser(unittest.TestCase):
  '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
  '''
  def setUp(self):
    '''
    Setup method to run before each test case
    '''
    self.new_user = User("Don","D0n")
  
  def tearDown(self):
    '''
    teardown method that does clean up after each test case
    '''
    User.user_list = []

  def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''

    self.assertEqual(self.new_user.userName,"Don")
    self.assertEqual(self.new_user.password,"D0n")
  
  def test_save_user(self):
    '''
    test_save_credential test case to test if the credential object is added to credentials_list
    '''
    self.new_user.saveUser() # saving the new contact
    self.assertEqual(len(User.user_list),1)

if __name__ == "__main__":
  unittest.main()