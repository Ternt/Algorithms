import pickle

class carRecord:
    def __init__ (self):
        self.DateofRegistration = None
        self.VehicleID = ""
        self.CarPlate = ""
        self.PurchasePrice = 0.00

ThisCar = carRecord()



CarFile = open('record.DAT', 'wb')
for i in range(100):
    ThisCar.DateofRegistration = input("DD/MM/YY| ")
    ThisCar.VehicleID = str(input("XXXXXX| "))
    ThisCar.CarPlate = str(input("XXX-XXX.XX| "))
    ThisCar.PurchasePrice = float(input("Price: "))
    pickle.dump(ThisCar)








    
    
    





    
        
                
        


        











        
