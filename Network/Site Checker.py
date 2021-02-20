import requests
import time

print("Site i.e ( https://google.com )")
url = str(input("Input a site: "))

print("Default per check is 5 seconds")

def check(req):
	if req >= 500:
		print("Server Error...")
	elif req >= 400:
		print("Client Error...")
	elif req >= 300:
		print("Redirects...")
	elif req >= 200:
		print("All good.")
	else:
		print("Error...")

while True:
	try:
		req = requests.get(url)
		req = int(req.status_code)
		res = check(req)
	except:
		print("Site Error...")
		break
	time.sleep(5)