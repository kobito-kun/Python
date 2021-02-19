import json
from collections import OrderedDict
from collections import Counter

location = input("Input .txt location (hello.txt): ")

file = open(location, 'r').read()

count = Counter(file)

for i in count:
	print(f"{i.capitalize()} : {count[i]}")