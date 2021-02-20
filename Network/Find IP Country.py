import requests
api1 = 'http://ip-api.com/json/'

#Extra stuff abt api:
json_response = {
    "query": "190.207.66.176",
    "status": "success",
    "continent": "South America",
    "continentCode": "SA",
    "country": "Venezuela",
    "countryCode": "VE",
    "region": "B",
    "regionName": "Anzoátegui",
    "city": "Barcelona",
    "district": "",
    "zip": "",
    "lat": 10.1362,
    "lon": -64.6862,
    "timezone": "America/Caracas",
    "offset": -14400,
    "currency": "VEF",
    "isp": "CANTV Servicios, Venezuela",
    "org": "CANTV Servicios, Venezuela",
    "as": "AS8048 CANTV Servicios, Venezuela",
    "asname": "CANTV Servicios, Venezuela",
    "mobile": false,
    "proxy": false,
    "hosting": false
}

print("""
1. Host
2. IP (HTTP/S Only)
""")
option = int(input("Enter an option: "))

def check(value):
	proxy = {'https': value}
	r = requests.get(str(api1) + str(value))
	r = r.json()
	r = r['country']
	return r

if option == 1:
	value = ''
	a = check(value)
	print(a)

elif option == 2:
	value = input("Input an ip: ")
	a = check(value)
	print(a)
else:
	print("Invalid Response")