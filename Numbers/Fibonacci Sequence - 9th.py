initial = int(input("Enter a integer: "))
seq = int(input("Times: "))
n1 = initial
n2 = initial

value = n2 + n1
value2 = value + n2

for i in range(seq):
	value3 = value2 + value
	temp = value2
	temp2 = value3
	value2 = temp2
	value = temp

print(value3)