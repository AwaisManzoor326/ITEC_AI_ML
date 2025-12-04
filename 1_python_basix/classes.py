class NewCar:
    
    def __init__(self, manufacturer, model):
        self.manufacName = manufacturer
        self.modelName = model
        
    def printDetails(self):
        print(f"Manufacturer: {self.manufacName}, Model: {self.modelName}")
        
        
myCar = NewCar("Toyota", "Corolla")
myCar.printDetails()