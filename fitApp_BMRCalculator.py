# Colin Mechaelsen 11/26/2024
# Fitness App, Calorie Calculator File
# This will be the File that houses the math and biometric componenets for the FitApp
import json

class BMR_Calculator:
    def __init__(self, User):
        self.User = User
        self.sex = User['Sex']
        self.age = User['Age']
        self.weight =  User['Weight']
        self.height = User['Height']
        
    def getSex(self):
        return self.sex

    def getAge(self):
        return self.age

    def getWeight(self):
        return self.weight

    def getHeight(self):
        return self.height

    def getBMR(self):
        if ((self.sex == 'M') or (self.sex == 'm')):
                bmr = 66 + (6.23 * self.weight) + (12.7 * self.height) - (6.8 * self.age)
        elif ((self.sex == 'F') or (self.sex == 'f')):
                bmr = 447.593 + (9.247 * (self.weight / 2.2)) + (3.098 * (self.height * 2.54)) - (4.330 * self.age)
        self.User['BMR'] = bmr
        return bmr


    
        
            


            
        
        
    
    
    

    