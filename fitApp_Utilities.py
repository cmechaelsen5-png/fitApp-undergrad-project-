import json

class Utilities:
    def __init__(self, User_ID):
        self.User_ID = User_ID
        
       
    
    def Load_User_File(self):
        data = f"{self.User_ID}.json"
        with open(f"{data}", "r") as f:
            User = json.load(f)
            
        return User
        
    def Save_User(self, User, User_ID):
        data = f"{User_ID}.json"
        with open(data, "w") as f:
            json.dump(User, f, indent=4)
        
        
        Accounts = f"Accounts.json"
        with open(Accounts, "r") as f:
            accounts = json.load(f)
            for Account in accounts:
                if Account['User_ID'] == User_ID and Account['Password'] == User['Password']:
                    Account.update(User)
                    
        with open(Accounts, "w") as f:
            json.dump(accounts, f, indent=4) 
                
            
                
                