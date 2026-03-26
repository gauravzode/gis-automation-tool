class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model= model
    def full_name(self):
        return f"{self.brand} {self.model}"
class ElectricCar (Car):
    def __init__(self, brand, model, batterysize):
        super().__init__(brand, model)
        self.batterysize = batterysize
    def full_name(self):
        return f"{self.brand} {self.model} with {self.batterysize} battery"
my_tesla= ElectricCar("Tesla", "S", "85kWh")
print(my_tesla.full_name())
     
#my_car= Car("toyota", "corolla")
#print(my_car.brand)
#print(my_car.model)
#print(my_car.full_name())
#my_car= Car("tata", "safari")
#print(my_car.brand)