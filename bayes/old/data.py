import requests
import csv

url = 'http://opendata-download-metobs.smhi.se/api/version/latest/parameter/19.json'
r = requests.get(url)
data = r.json()

JSON = 'application/json'
get_json = lambda link : requests.get(filter(lambda e: e['type'] == JSON, link)[0]['href']).json()
for station in data['station'][4:5]:
	s_name = station['name']
	# print s_name
	s_data = get_json(station['link'])
	s_data = get_json(s_data['period'][0]['link'])
	# s_data = get_json(s_data['link'])
	csvfile = requests.get(s_data['data'][0]['link'][0]['href']).content
	reader = csv.reader(csvfile)
	with open('tmp.txt','w') as f:
		for row in reader:
			f.write(','.join(row))
	# with open('tmp.txt','w') as f:
	# 	f.write(csvfile)
	# print station['longitude'],station['latitude']
	# for k in station:
	# 	print k