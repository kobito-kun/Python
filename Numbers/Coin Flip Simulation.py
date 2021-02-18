import random

times = int(input("How many times do u want to flip? "))
head = []
tails = []

for i in range(times):
	n = random.randint(1,2)
	if n == 1:
		head.append(n)
	else:
		tails.append(n)

print(f"""
Times ran: {times}
Heads: {len(head)}
Tails: {len(tails)}
""")