
class BMI_Calculator:
    def __init__(self, User):
        self.User = User
        self.height = User['Height']
        self.weight = User['Weight']
        
        
    def getBMI(self):
        bmi = (((self.weight) / (self.height**2)) * 703)
        self.User['BMI'] = bmi
        return bmi
        
    