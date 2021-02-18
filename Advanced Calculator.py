print("""
1. Normal
2. Semi
3. Advanced
""")
option = int(input("Enter one of the options above: "))
nums = []

if option == 2:
	g = True
	while g == True:
		v = float(input("Enter a number: "))
		nums.append(v)
		k = input("Continue? (Yes or No): ")
		if k == "Yes":
			g = True
		elif k == "No":
			g = False
		else:
			pass
	op = input("Operator? ( +, -, *, / ): ")
	if op == "+":
		total = 0
		for i in nums:
			total += i
		print(f"\n{total}")
	elif op == "-":
		total = 0
		for i in nums:
			total -= i
		print(f"\n{total}")
	elif op == "*":
		total = 1
		for i in nums:
			total *= i
		print(f"\n{total}")
	elif op == "/":
		total = 1
		for i in nums:
			total /= i
		print(f"\n{total}")	
	else:
		pass
elif option == 1:
	pass
elif option == 3:
	pass
else:
	pass