import json

class User_LogIn:
    def __init__(self, User_ID, User_Password):
        self.User_ID = User_ID
        self.User_Password = User_Password
        
    
    def Get_UserInfo(self):
        User_ID = input("Please enter your User ID or email: ")
        User_Password = input("Please enter your account password: ")
        return User_ID, User_Password
        
    def Load_User_Account(self, User_ID, User_Password):
        try:
            with open(f"{User_ID}.json", "r") as f:
                User = json.load(f)
                if f"{User['ID']}" == User_ID and f"{User['Password']}" == User_Password:
                    print(f"Welcom Back {User['ID']}")
                    return User
                else:
                    print("You appear to have entered the wrong User ID or Password, Please try again.")
                    return None
                    
        except:
            FileNotFoundError
            while True:
                print("Account file not found, perhaps you there was a typo. Please try again.")
                User_ID = input("Please enter your User ID or email: ")
                User_Password = input("Please enter your password: ")
                if User_ID and User_Password:
                    break
                return User_ID, User_Password
            
            

