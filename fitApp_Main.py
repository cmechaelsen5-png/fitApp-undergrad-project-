import json
from fitApp_CreateAccount import Create_Account
from Get_Bios import Get_Bios
from fitApp_BMICalculator import BMI_Calculator
from fitApp_BMRCalculator import BMR_Calculator
from fitApp_DCICalculator import DCI_Calculator
from fitApp_MacroCalculator import Macro_Calculator
from fitApp_Utilities import Utilities
from fitApp_LogIn import User_LogIn



def main():
    action = input("Would you like to [C]reate an account, or [L]ogin to an existing account?: ")
    while action.lower() not in ['l', 'c']:
        action = input("Would you like to [C]reate an account, or [L]ogpin to an existing account?: ")
    if action == 'c':
        User_ID, User_Password = Create_Account.Set_User()
        new_account = Create_Account(User_ID, User_Password)
        new_account.Save_NewUser(User_ID)
        utility = Utilities(User_ID)
        User = utility.Load_User_File()
        account_bios = Get_Bios(User)
        updated_bios =  account_bios.Update_User_Bios()
        save = utility.Save_User(User, User_ID)
        User
        bmr = BMR_Calculator(User)
        User_bmr = bmr.getBMR()
        save = utility.Save_User(User, User_ID)
        User
        bmi = BMI_Calculator(User)
        User_bmi = bmi.getBMI()
        save = utility.Save_User(User, User_ID)
        User
        dci = DCI_Calculator(User)
        dci.get_DCI()
        save = utility.Save_User(User, User_ID)
        User
        macros = input("Would you like to [B]ulk, [C]ut, or [R]ecomp body mass?: ")
        while macros.lower() not in ['b', 'c', 'r']:
            macros = input("Would you like to [B]ulk, [C]ut, or [R]ecomp body mass?: ")
        Umacros = Macro_Calculator(User) 
        if macros.lower() == 'b':
            User_Macros = Umacros.standardBulk_Macros()
            save = utility.Save_User(User, User_ID)
            User
        elif macros.lower() == 'c':
            User_Macros = Umacros.standardCut_Macros()
            save = utility.Save_User(User, User_ID)
            User
        elif macros.lower() == 'r':
            User_Macros = Umacros.Recomp_Macros()
            save = utility.Save_User(User, User_ID)
            User
    elif action.lower() == 'l':
        log_in = User_LogIn("", "")
        User_ID, User_Password = log_in.Get_UserInfo()
        User = log_in.Load_User_Account(User_ID, User_Password)
        print(f"User data: {User}")
    

if __name__ == "__main__":
    main()