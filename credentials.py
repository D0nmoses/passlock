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
  
  def newCredential(self,userAccount,site,password):
    credential = Credentials(userAccount,site,password):
  
  def addCustomCredential(self):
    userAccount = input("Enter username for the account: \n")
    site = input("Enter the site whose credentials are being saved: \n")
    password = input("Enter your desired password")
    newCredential(userAccount,site,password)
    add_credential('credential.csv',userAccount,site,password)
  
  def add_credential(filename,userAccount,site,password):
    '''
    add_user method writes the new user details to an external file
    '''
    with open(filename,'a') as csv_file:
      a = csv.writer(csv_file,delimiter = ',')
      data = [userAccount,site,password]
      a.writerows(data)
  