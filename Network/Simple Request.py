import requests

link = 'https://coronavirus-19-api.herokuapp.com/countries/world'
http = '212.188.66.26:3128'
https = '212.188.66.26:3128'

proxy = {
	'http': http,
	'https': https,
}

r = requests.get(link)
r = r.json()


print(f"""
=== World ===
Cases : {r['cases']}
Cases Today : {r['todayCases']}
Deaths : {r['deaths']}
Deaths Today: {r['todayDeaths']}
Recovered : {r['recovered']}
Active : {r['active']}
Critical : {r['critical']}
""")

#print(r.json())