class Emplyoo:
 name :str
 age:int =0
 timlön:int=0
 antaltimmar:int=0

def __init__(self,name,age,timlön,antaltimmar):
        self.name=name
        self.age= age
        self.timLön=timlön
        self.antaltimmar=antaltimmar
def calculateSalary(self):
    salary=self.timlön*self.antaltimmar    
    if self.age>=25 and self.age<=45:
        salary*=1.05
    elif self.age>45:
        salary*=1.06
    if self.nama=="stafen":
        salary+=220
        return salary   
     