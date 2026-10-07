class Macro_Calculator:
    def __init__ (self, User):
        self.User = User
        self.dci = User['DCI']
    
    def Recomp_Macros(self):
        protein = ((self.dci * 0.3) / 4)
        carbs = ((self.dci * 0.5) / 4)
        fats = ((self.dci * 0.2) / 9)
        self.User['Macros']['Protein'] =  protein 
        self.User['Macros']['Carbs'] =  carbs 
        self.User['Macros']['Fats'] =  fats 
        
        return protein, carbs, fats
    
    def standardCut_Macros(self):
        dci = (self.dci - 500)
        protein = ((self.dci * 0.35) / 4)
        carbs = ((self.dci * 0.45) / 4)
        fats =  ((self.dci * 0.2) / 9 )
        self.User['Macros']['Protein'] =  protein 
        self.User['Macros']['Carbs'] =  carbs 
        self.User['Macros']['Fats'] =  fats 
        return protein, carbs, fats
    
    def standardBulk_Macros(self):
        dci = (self.dci + 500)
        protein = ((self.dci * 0.3) / 4)
        carbs = ((self.dci * 0.5) / 4)
        fats = ((self.dci * 0.2) / 9)
        self.User['Macros']['Protein'] =  protein 
        self.User['Macros']['Carbs'] =  carbs 
        self.User['Macros']['Fats'] =  fats 
        return protein, fats, carbs
        
    
    def Maintanence_Macros(self):
        protein = ((self.dci * 0.25) / 4)
        carbs = ((self.dci * 0.5) / 4)
        fats = ((self.dci * 0.25) / 9)
        self.User['Macros']['Protein'] =  protein 
        self.User['Macros']['Carbs'] =  carbs 
        self.User['Macros']['Fats'] =  fats 
        return protein, fats, carbs
