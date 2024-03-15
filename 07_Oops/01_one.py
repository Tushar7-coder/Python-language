class car:
	wheels =4 #class variable
	def __init__(self):
		self.mil = 10 #instance variable
		self.com="BMW"
c1=car()
c2=car()
c1.mil = 17	
print(c1.mil)
car.wheels = 5 
print(c1.wheels)
