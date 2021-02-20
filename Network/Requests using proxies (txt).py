import requests
import json

f = open('proxies.txt', 'r')
f = list(f)

link = 'https://api.ipify.org?format=json'
#http = str(f[0].strip('\n'))
https = str(f[0].strip('\n'))

for i in f:
	i = i.strip('\n')
	proxy = {'https':https}
	https = str(i)
	try:
		r = requests.get(link, proxies=proxy)
		r = r.json()
		print(f"Your ip is: {r['ip']}")
	except:
		print("Failed Connection. (Probably Proxy not working)")

#print(r.json())