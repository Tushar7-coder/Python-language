class Student:
	school = "ssvm"
	def __init__(self,m1,m2,m3):
		self.m1 =m1
		self.m2 = m2
		self.m3 = m3
	def avg(self):
		return (self.m1+self.m2+self.m3)/3
	def get_m1(self):
		return self.m1
	def set_m1(self,value):
		self.m1 = value
	@classmethod	
	def info(cls):
		return cls.school
	# def info2():
	# 	print("Tushar") 

s1=Student(22,33,48)
print(s1.avg())
s2 = Student(67,45,78)
s2.set_m1(99)
print(s2.m1)
print(Student.info())
print(s2.info2)
		