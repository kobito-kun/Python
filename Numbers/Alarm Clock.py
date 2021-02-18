import time
import os
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
	value = value.split(':')
	v1 = float(value[0]) * 3600
	v2 = float(value[1]) * 60
	v3 = float(value[2])
	base = v1 + v2 + v3
	return base

def sound():
	os.system("start olli.mp3")

if option == 1:
	value = float(input("Enter a value: "))
	k = input("H/M/S?: ")
	j = convertToSeconds(k, value)
	print(f"The alarm will sound in '{j}' seconds.")
	for i in range(int(j)):
		print(f"Alarm will sound in { j-i }")
		time.sleep(1)
	#time.sleep(int(j))
	sound()
elif option == 2:
	print("HR/MIN/SEC (1:23:12)")
	k = input("Input a time: ")
	j = calculateAMPMToSeconds(k)
	print(f"The alarm will sound in {j}seconds.")
	for i in range(int(j)):
		print(f"Alarm will sound in { j-i }")
		time.sleep(1)
	#time.sleep(int(j))
	sound()