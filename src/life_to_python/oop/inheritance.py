class Vehicle:
    def __init__(self,name,model,brand):
        self.name = name
        self.model = model
        self.brand = brand
        
        
    def starts(self):
        print(f"The {self.name}, with model: {self.model} and brand: {self.brand}")
        
        

class Truck(Vehicle):
    def __init__(self,name,model,brand,size):
        super().__init__(name,model,brand)
        self.speed = "40 kmp/h"
        self.size = size
    
    def truck_size(self):
        print(f"the truck size is {self.size}")
   
    def truck_speed(self):
        print(f"the truck speed is slow upto {self.speed}")
        
 
truck1 = Truck("magonware","2012","Hyunshi","20m")

        
                
    
    