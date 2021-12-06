import requests
import json

# id = input("Enter student id: ")
# URL = "http://127.0.0.1:8000/stuinfo/"+id

# r = requests.get(url = URL)

# print(r.json())
URL = "http://127.0.0.1:8000/stucreate/"
data = {
	'name': 'kfjlsadkjf',
	'roll': 1983,
	'city': 'jamalpur'
}
json_data = json.dumps(data)
r = requests.post(url = URL, data = json_data)

data = r.json()
print(data)