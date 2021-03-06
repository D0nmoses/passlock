
class Credentials:
  '''
  class Credentials defines properties of a credential
  '''
  credentials_list = []

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
    Credentials.credentials_list.append(self)
  
  @classmethod
  def viewCredentials(cls):
    '''
    method returns a list of all input credentials
    '''
    return cls.credentials_list
  
  @classmethod
  def findCredBySiteName(cls,userSite):
    '''
    method findCredBySiteName returns the credential that matches the site passed
    '''
    for credential in cls.credentials_list:
      if credential.userSite == userSite:
        return credential
  
