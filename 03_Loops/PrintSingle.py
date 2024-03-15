Original = input("Enter a word ")
for char in Original :
	if char.count(char) == 1:
		print(char)
		break

