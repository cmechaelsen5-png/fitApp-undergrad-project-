
import json


class Get_Bios:
    def __init__(self, User):
        self.User = User
        self.valid = False
        
    def Get_Age(self):
        self.User['Age'] = int(input("Please enter your age in years: ")) 
    
    def Get_Sex(self):
        self.User['Sex'] = input("Please enter your sex, [M] for male, [F] for female: ")
        
    
    def Get_Height(self):
        while not self.valid:
            try:
                self.User['Height'] = int(input("Please enter your height in inches: ")) 
                self.valid = True              
            except ValueError as e:
                print("It seems you've entered an improper value, please enter your height in inches, as an integer value!")
        
    
    def Get_Weight(self):
        self.User['Weight'] = int(input("Please enter your weight in pouds: "))
        
    
    def Get_ActLvl(self):
        self.User['Act_lvl'] = int(input("Please enter the number of times you workout per week: "))
    
    def Update_User_Bios(self):
        self.Get_Age()
        self.Get_Sex()
        self.Get_Height()
        self.Get_Weight()
        self.Get_ActLvl()