from user import User
# print('hello world')
# from credentials import Credentials

def createUser(username,password):
  '''
  createUser method creates an instance of class User
  '''
  new_user = User(username,password)
  return new_user

def saveUser(user):
  '''
  saveUser method saves the new user instance in user_list array
  '''
  User.saveUser(user)

def checkUser(username,password):
  '''
  checkUser method verifies whether user credentials are correct to login
  '''
  isUser = User.userExists(username,password)
  return isUser

def login():
  '''
  login method verifies whether a user can login
  '''
  username = input("Please enter your username: \n")
  password = input("Please enter your password: \n")
  isUser = checkUser(username,password)
  if(isUser):
    menu()
  else:
    print("Incorrect username or password")
    login()

def register():
  '''
  register method signs up new users
  '''
  username = input("Enter your preferred username: \n")
  password = input("Enter your preferred password: \n")
  passwordAgain = input("Enter the password again: \n")
  if(password == passwordAgain):
    new_user = createUser(username,password)
    saveUser(new_user)
    print(f'Welcome {username}')
    print("Please enter login details:")
    login()
  else:
    register()
  
  def menu():
    '''
    method menu displays options for accessing features 
    '''
    
def main():
  # print('')
  print("*"*40)
  print("Welcome to Password Locker \nHow may we assist you today?")
  print("\n A:Register \n B:Login \n C:Exit \n")
  first_choice = input()
  if(first_choice == "A" or first_choice == "a"):
    register()
  elif(first_choice == "B" or first_choice == "b"):
    login()
  elif(first_choice == "C" or first_choice =="c"):
    return 0
  
if __name__ == '__main__':
    main()