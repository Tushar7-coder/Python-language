def greet():
	print("Hello")
#greet()
def add(a,b):
	return a+b
#print(add(3,4))
def update(x):
	x=8
	print(x)
#update(11)
def person(name , age):
	print(name,age)
#person(name = "Tushar",age =22)
def add(*args):
	c= sum(args)
	print(c)
#add(1,2,3,4,5,6)
def person(name,**data):
	print(name)
	print(data)
	for i,j in data.items():
		print(i,j)
person(name = "Navin",age =22,city="Mumbai",mob =8917355202)		 

		



	

	