
class DCI_Calculator:
    def __init__(self, User):
        self.User = User
        self.bmr = User['BMR']
        self.Act_lvl = User['Act_lvl']
        
        
    def get_DCI(self):
        if self.Act_lvl <= 1:
            dci = (self.bmr * 1.2)
            self.User['DCI'] = dci
            return dci
            
        elif self.Act_lvl < 3:
            dci = (self.bmr * 1.375)
            self.User['DCI'] = dci
            return dci
            
        elif self.Act_lvl >= 3 and self.Act_lvl <= 5:
            dci = (self.bmr * 1.55)
            self.User['DCI'] = dci
            return dci
            
        elif self.Act_lvl >= 6:
            dci = (self.bmr * 1.725)
            self.User['DCI'] = dci
            return dci
            
       # return dci
        #self.User['DCI'] = float(self.dci)
        
    #def set_DCI(self, User):
        
