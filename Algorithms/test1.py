import random

init = 25
race_limit = 5
horses = []

# assigning value to horses ( secret )
for i in range(init):
	horse = random.randint(1, 100)
	horses.append(horse)

# Race 5 times to get a,b,c,d,e

a = []
b = []
c = []
d = []
e = []

for horse in range(len(horses)):
	if len(a) != race_limit:
		a.append(horses[horse])
	elif len(b) != race_limit:
		b.append(horses[horse])
	elif len(c) != race_limit:
		c.append(horses[horse])
	elif len(d) != race_limit:
		d.append(horses[horse])
	else:
		e.append(horses[horse])

# Sort from low to high
a = sorted(a)
b = sorted(b)
c = sorted(c)
d = sorted(d)
e = sorted(e)

attributes = [e, d, c, b, a]

print("==== Sorted ====")
for a in attributes:
	print(a)
print("================\n")

# using bubble sort to sort:

print("initial: ", attributes)

for j in range(len(attributes) - 1):
		for i in range(0, len(attributes)-j-1):
			if attributes[j][4] < attributes[j + 1][4]:
				attributes[j], attributes[j+1] = attributes[j+1], attributes[j]
			else:
				pass
			
print("sorted: ", attributes)

print("\n" * 3)
# Debugging
print(a)
print(b)
print(c)
print(d)
print(e)
