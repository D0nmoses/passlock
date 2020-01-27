import unittest

from credentials import Credentials

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
    self.new_cred = Credentials("d0nM","Twtter","d0nM")
  
  def tearDown(self):
    '''
    teardown method that does clean up after each test case
    '''
    Credentials.credentials_list = []

  def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''

    self.assertEqual(self.new_cred.userAccount,"d0nM")
    self.assertEqual(self.new_cred.userSite,"Twitter")
    self.assertEqual(self.new_cred.password,"d0nM")
  
  def test_save_credential(self):
    '''
    test_save_credential test case to test if the credential object is added to credentials_list
    '''
    self.new_cred.saveCredential() 
    self.assertEqual(len(Credentials.credentials_list),1)

if __name__ == "__main__":
  unittest.main()
