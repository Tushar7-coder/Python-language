class Student :
	def __init__(self,name,roll_no):
		self.name = name
		self.roll_no = roll_no
		self.lap = self.laptop()
	def show(self):
		print(self.name,self.roll_no)
		self.lap.show()
	class laptop:
		def __init__(self):
			self.brand = "Hp"
			self.cpu = "15"
			self.ram =8
		def show(self):
			print(self.brand,self.cpu,self.ram)	

s1= Student("Navin",2)
s2=Student("Tushar",60)
# s1.show()
lap1 = s1.lap
lap2 =s2.lap
s1.show()

