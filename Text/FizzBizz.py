import random

#Fizz Buzz - Write a program that prints the numbers from 1 to 100. But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. For numbers which are multiples of both three and five print “FizzBuzz”.

def finding(num):
	if num % 5 == 0 and num % 3 == 0:
		return "FizzBuzz"
	elif num % 3 == 0:
		return "Fizz"

	elif num % 5 == 0:
		return "Buzz"
	else:
		return num

for i in range(1,101):
	a = finding(i)
	print(a)