import time

value = float(input("Enter a value: "))
print("""
Enter an option:
1. Intervals
2. AM/PM""")
option = int(input("Enter an option: "))

def convertToSeconds(param, value):
	if param == "H":
		value *= 3600
		return value
	elif param == "M":
		value *= 60
		return value
	elif param == "S":
		value = value
		return value

def calculateAMPMToSeconds(value):
	#Calculate value

def sound():


if option == 1:
	k = input("H/M/S?: ")
	j = convertToSeconds(k, value)
	time.sleep(int(j))
	sound()
elif option == 2:
	k = input("Input a time: ")
	j = calculateAMPMToSeconds(k)
	time.sleep(int(j))
	sound()