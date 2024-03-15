import math
def circle_stat(radius):
	area = round(math.pi*radius**2)
	circumference = 2*math.pi*radius
	return area , circumference

print(circle_stat(4))
