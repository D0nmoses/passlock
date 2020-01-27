import random
import pyperclip
import user
import csv


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
    credential = Credentials(userAccount,site,password)

  def add_credential(filename,userAccount,site,password):
    '''
    add_credential method writes the new credential details to an external file
    '''
    with open(filename,'a') as csv_file:
      a = csv.writer(csv_file,delimiter = ',')
      data = [userAccount,site,password]
      a.writerows(data)

  def generatePassword():
    symbol = 0
    lower = 0
    upper = 0
    number = 0
    count = 0
    password = []

    length = input("How many characters do you need in your password?")

    while count < length:
        rand = random.randint (0,3)
        if rand == 0:
            lower += 1
            b = int(random.randint (97,123))
            password.append(b)
        elif rand == 1:
            upper += 1
            b = random.randint (65,91)
            password.append(b)
        elif rand == 2:
            number += 1
            b = random.randint (48,58)
            password.append(b)
        elif rand == 3:
            r = random.randint(0,2)
            symbol += 1
            if r == 0:
                b = random.randint (33,48)
                password.append(b)
            elif r == 1:
                b = random.randint (91,97)
                password.append(b)
            elif r == 2:
                b = random.randint (123,126)
                password.append(b)
        count += 1

        #convert ascii code to characters
        word = "".join([chr(c) for c in password])

        #copy pass to clipboard
        pyperclip.copy(word)

        #print the result
        print ("Random password of length %s is: \n" % length)
        print(word)
        return(word)

  def addCustomCredential(self):
    userAccount = input("Enter username for the account: \n")
    site = input("Enter the site whose credentials are being saved: \n")
    password = input("Enter your desired password")
    newCredential(userAccount,site,password)
    add_credential('credential.csv',userAccount,site,password)
    print("Credentials saved")
    user.menu()
  
  def addGeneratedCredential(self):
    userAccount = input("Enter username for the account: \n")
    site = input("Enter the site whose credentials are being saved: \n")
    password = generatePassword()
    newCredential(userAccount,site,password)
    add_credential('credential.csv',userAccount,site,password)
    print("Credentials saved")
    user.menu()
    
  
  def add_credential(filename,userAccount,site,password):
    '''
    add_user method writes the new user details to an external file
    '''
    with open(filename,'a') as csv_file:
      a = csv.writer(csv_file,delimiter = ',')
      data = [userAccount,site,password]
      a.writerows(data)
  
  @classmethod
  def viewCredentials(cls):
    with open("credentials.csv") as f:
      reader = csv.reader(f)
      print(next(reader))

  @classmethod
  def deleteCredentials(cls):
    choice = input("Which site credentials do you wish to delete? \n")
    with open("credentials.csv") as f:
      


  