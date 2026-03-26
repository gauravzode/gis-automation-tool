class Car:
    total_car = 0
    
    
    def __init__(self,brand, model):
        self.__brand = brand
        self.__model = model
        Car.total_car +=1
        
    def get_brand(self):
        return self.__brand + "!"
    
    def full_name(self):
        return f"{self.__brand} {self.__model}"
       
    def fuel_type(self):
        return "Petrol or Diesel"
    
    @staticmethod
    def general_description():
        return "My Car is special"
     
    @property
    def model (self):
         return self.__model
     
class ElectricCar(Car):
     def __init__(self, brand, model, battery_size):
         super().__init__(brand, model)
         self.battery_size = battery_size
            
     def fuel_type(self):
            return "Electric charge"
        
        
my_tesla = ElectricCar("Tesla", "Model S", "85 KWh")
#print(my_tesla.fuel_type())

my_car = Car ("Tata", "Safari")
#my_car.model = "City"
Car ("Tata", "Nexon")

safari = Car("Tata", "Safari")

#print (isinstance(my_tesla, Car))
#print (isinstance(my_tesla, ElectricCar))
#print (my_car.model)
#print ( safari.fuel_type())

#print (my_car.general_description())
#print (Car.general_description())

#print (Car.total_car)
#print(my_tesla.full_name ())   
print (my_tesla.get_brand())   
#my_car = Car("Toyota", "Corolla")
#print(my_car.brand)
#print(my_car.model)
#print(my_car.full_name())

class Battery:
    def battery_info (self):
        return "This is Battery"
    
class Engine:
    def engine_info (self):
        return "This is Engine"
    
class ElectricCarTwo(Battery,Engine, Car):
    pass

my_new_tesla = ElectricCarTwo("Tesla", "Model S")
print (my_new_tesla.battery_info())
print (my_new_tesla.engine_info())
