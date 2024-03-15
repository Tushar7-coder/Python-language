a= 10
print(id(a))
def something():
	a =9
	x = globals()['a']
	print(id(x))
	print("in ",x)
	globals()['a']=15
something()	

