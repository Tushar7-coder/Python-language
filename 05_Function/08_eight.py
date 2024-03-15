def print_kwargs(name , age ):
	print("Name ",name,"Age: ",age)
print_kwargs("tushar", 22)
print_kwargs( age =22,name = "Liku" )
print_kwargs(name = "Liku" , age =22)
print_kwargs(age = 21, name = "pratik")	


def print_kwargs(**kwargs):
	for key,value in kwargs.items():
		print(f"{key}:{value}")

print_kwargs( age =22,name = "Liku" )
print_kwargs(name = "Liku" , age =22)
print_kwargs(age = 21, name = "pratik", gender = "male")		