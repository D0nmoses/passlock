import csv
# from credentials import Credentials

class  User:
  '''
  Class that generates instance of users
  '''
  user_list = []


  def __init__(self,username,password):
    '''
    init_ method that defines properties for our objects
    '''
    
    self.username = username
    self.password = password

  def saveUser(self):
    '''
    saveUser method saves the user properties to user_list
    '''
    User.user_list.append(self)

  @classmethod
  def userExists(cls,username,password):
    '''
    userExists method checks whether user details exist in the user_list array
    '''
    for user in User.user_list:
      if(user.username == username and user.password == password):
        return True
      else:
        return False

  
  