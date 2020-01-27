import csv
from credentials import Credentials

class  User:
  '''
  Class that generates instance of users
  '''
  def __init__(self,username,password):
    '''
    init_ method that defines properties for our objects
    '''
    
    self.username = username
    self.password = password

  def enter_password(self):
    '''
    enter_password method checks if password entered matches confirmation password and return the password
    '''
    while True:
      password = input("Enter password: \n")
      passwordAgain = input("Confirm password: \n")
      if password != passwordAgain:
        print("Password and confirmation do not match")
      else: return password

  def add_user(filename,username,password):
    '''
    add_user method writes the new user details to an external file
    '''
    with open(filename,'a') as csv_file:
      a = csv.writer(csv_file,delimiter = ',')
      data = [username,password]
      a.writerows(data)
    
  def new_user(username,password):
    user = User(username,password)
  
  def register():
    '''
    register method allows user to store registation details
    '''
    username = input("Enter your preferred username: \n")
    password = enter_password()
    new_user(username,password)
    add_user('user.csv',username,password)
    login()

  def login():
    username = input("Enter your username: \n")
    password = input("Enter your password: \n")
    menu()
  
  def menu(self):
    menu_choice = print("What would you like to do today: \n A: View my credentials \n B: Add custom credential \n C: Add credential with auto-generated password \n D: Delete a credential")
    if(menu_choice == "A" or menu_choice == "a"):
      Credentials.viewCredentials()
    elif(menu_choice == "D" or menu_choice == "d"):
      Credentials.deleteCredential()
    elif(menu_choice == "B" pr menu_choice == "b"):
      Credentials.addCustomCredential()
    elif(menu_choice == "C" or menu_choice == "c"):
      Credentials.addAutoCredential()

  
  