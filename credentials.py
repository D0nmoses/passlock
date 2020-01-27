class Credentials:
  '''
  class Credentials defines properties of a credential
  '''
  credetials_list = []

  def __init__(self,userAccount,userSite,password):
    '''
    method init initializes credentials properties
    '''
    self.userAccount = userAccount
    self.userSite = userSite
    self.password = password
  
  def saveCredential(self):
    '''
    method saveCredentials saves credential details to credentials list array
    '''
    Credentials.credetials_list.append(self)
  
  @classmethod
  def viewCredentials(cls):
    '''
    method returns a list of all input credentials
    '''
    return cls.credetials_list
  
  