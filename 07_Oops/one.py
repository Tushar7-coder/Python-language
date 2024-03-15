class Car:
	def __init__(self,userbrand,usermodel):
		self.brand = userbrand
		self.model = usermodel
	def fullname(self):
		return f"{self.brand} {self.model}"	
	def car_type(self):
		return "petrol or disel"

class ElectricCar(Car):
	def __init__(self,userbrand,usermodel,userbattery_size):
		super().__init__(userbrand,usermodel)
		self.battery_size = userbattery_size
	def car_type(self):
		return "Electric charge"
	

safari = Car("Tata","Safari")
tesla = ElectricCar("Tesla","Model s",85)
print(tesla.car_type())
print((safari.car_type()))
my_tesla = ElectricCar("Tesla","Model S","65kw")
print(my_tesla.model)
print(my_tesla.fullname())

my_car=Car("Tata","Safari")
print(my_car.brand)
print(my_car.model)
print(my_car.fullname())

my_car2 = Car("Toyota","Fortuner")
print(my_car2.brand)
print(my_car2.model)

