class Credentials:
  '''
  A class that generates new instances of credentials
  '''

  def __init__(self,userAccount, site, password):
    '''
    init property that defines the properties of our objects
    '''
    self.userAccount = userAccount
    self.site = site
    self.password = password
  
  