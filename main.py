from user import User
from credentials import Credentials

print("********** Welcome to Password Locker **********")
decision = input("Would you like to register or login? \n A: Register \n B: Login \n" )

if(decision == "A" or decision == "a"):
  register()
else:
  login()
