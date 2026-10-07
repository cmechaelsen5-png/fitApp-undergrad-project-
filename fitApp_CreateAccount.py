
import json
import os
class Create_Account:
    def __init__(self, User_ID, User_Password):
        self.User_ID = User_ID
        self.User_Info = {
            "User_ID": User_ID,
            "Password": User_Password,
            "Age": '',
            "Weight": '',
            "Height": '',
            "Sex": '',
            "Act_lvl": '',
            "BMI": '',
            "BMR": '',
            "DCI": '',
            "Macros" : {},  
        }
    
    @staticmethod
    def Set_User():
        User_ID = input("Please enter your user ID or email: ")
        User_Password = input("Please enter your user password: ")
        return User_ID, User_Password

    def Save_NewUser(self, User_ID):
        User = f"{User_ID}.json"
        if not os.path.exists(User):
            with open(User, "w") as f:
                json.dump(self.User_Info, f, indent=4)
        else:
            print(f"File already exists for {User_ID}")
            
        with open("Accounts.json", "r") as f:
            Accounts = json.load(f)
        
        Accounts.append(self.User_Info)
        with open("Accounts.json", "w") as f:
            json.dump(Accounts, f, indent=4)
        print(f"User info has been saved to Accounts, and a new account has been created for {self.User_ID}")

        