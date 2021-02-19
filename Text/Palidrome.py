string = str(input("Input a word: "))

reversed = string[::-1]

if reversed.lower() == string.lower():
	print("True")
else:
	print("False")