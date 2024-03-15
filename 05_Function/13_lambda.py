add = lambda a,b: a+b
# print(add(3,4))
nums = [3,2,6,8,4,6,2,9]
def is_even(n):
	if n % 2 ==0:
		return True
evens = list(filter(is_even,nums))
print(evens)
evens2 = list(filter(lambda n : n%2 == 0, nums))
print(evens2)
# reduce
from functools import reduce
sum = reduce(lambda a,b : a+b,evens2)
print(sum)
	