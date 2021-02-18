import math
value = int(input("Input an integer: "))

#If n is even, divide it by 2. If n is odd, multiply it by 3 and add 1.

while value > 1:
	if value % 2 == 0:
		value /= 2
		print(math.trunc(value), end=' ')
	else:
		value *= 3
		value += 1
		print(math.trunc(value), end=' ')

print(math.trunc(value), end='')