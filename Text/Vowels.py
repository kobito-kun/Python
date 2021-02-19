u = str(input("Input words / sentences: "))

u = u.lower()
arr = u.split(" ")
g = ['a', 'e', 'i', 'o', 'u']

total = 0
ac = 0
ec = 0
ic = 0
oc = 0
uc = 0

def checkVow(s):
	if s == g[0]:
		global ac
		ac += 1
	elif s == g[1]:
		global ec
		ec += 1
	elif s == g[2]:
		global ic
		ic += 1
	elif s == g[3]:
		global oc
		oc += 1
	else:
		global uc
		uc += 1

for i in range(len(arr)):
	s = list(arr[i])
	for v in range(len(s)):
		if s[v] in g:
			total += 1
			checkVow(s[v])
		else:
			pass

print(f"""
Total = {total}
a = {ac}
e = {ec}
i = {ic}
o = {oc}
u = {uc} 
""")
### This method only seems to support words 5+ chars
#	for v in range(len(vowels)):
#		if len(s) < len(vowels):
#			if vowels[v] == s[v]:
#				print(vowels[v])
#			else:
#				pass
#		else:
#			pass