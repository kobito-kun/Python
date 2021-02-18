value = int(input("Enter a number: "))
listOfPrime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

for i in listOfPrime:
	if i < value:
		calc = value % i
		if calc >= 1:
			pass
		elif calc == 0:
			print(f"The prime number of {value} is {i}")
	elif value == i:
		print(f"The prime number of {value} is {i}")
	elif i > value:
		pass
	else:
		print("Value has no prime numbers")