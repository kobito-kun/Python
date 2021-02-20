import requests

link = 'http://httpbin.org/ip'
http = '212.188.66.26:3128'
https = '212.188.66.26:3128'

proxy = {
	'http': http,
	'https': https,
}

r = requests.get(link, proxies=proxy)
r = r.json()


print(r)

#print(r.json())