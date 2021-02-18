value = int(input("Enter a number: "))
listOfPrime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
prime = []

for i in listOfPrime:
	if i < value:
		calc = value % i
		if calc >= 1:
			pass
		elif calc == 0:
			prime.append(i)
	elif value == i:
		prime.append(i)
	elif i > value:
		pass
	else:
		print("Value has no prime numbers")

for i in prime:
	y = True
	while y == True:
		print("\n" + "=====" + str(i) + "=====" + "\n")
		x = input("Type 'Yes' to continue\nType 'No' to stop.\n\n")
		if x == 'Yes':
			y = False
		elif x == 'No':
			y = True
		else:
			print("Bad Value")

print("Value has no / more prime.")