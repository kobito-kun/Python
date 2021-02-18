import math

value = float(input("Enter a value: "))
theList = [("Penny",0.01),("Nickle",0.05),("Dime",0.10), ("Quarter",0.25)]

for u, i in theList:
	temp = value / i
	temp = math.ceil(temp)
	print(f"You'll need {temp} {u}")