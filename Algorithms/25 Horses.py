import random

init = 25
race_limit = 5
horses = []

# assigning value to horses ( secret )
for i in range(init):
	horse = random.randint(0, 1000)
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

attributes = [a,b,c,d,e]

print("==== Sorted ====")
for a in attributes:
	print(a)
print("================\n")

# using bubble sort to sort:

for i in range(len(attributes) - 1):
		for j in range(0, len(attributes)-i-1):
			if attributes[j][4] < attributes[j + 1][4]:
				attributes[j], attributes[j+1] = attributes[j+1], attributes[j]
			else:
				pass

e = attributes[4]
d = attributes[3]
c = attributes[2]
b = attributes[1]
a = attributes[0]

top1 = a[4]

array = [a[3], a[2], b[4], b[3], c[4]]

result = sorted(array)

top2 = result[4]
top3 = result[3]

print("==== Sorted ====")
print(a)
print(b)
print(c)
print(d)
print(e)
print("================")

print(f"""
top1: {top1}
top2: {top2}
top3: {top3}
""")