
import json

with open("final.json") as f:
	people = json.load(f)

with open("us_cities.json") as f:
	cities = json.load(f)

for person in people['results']:

	found = False

	for city in cities['cities']:

		if person['statedisplaynameoflastcontact'] == city['state_id']:
			found = True
			person['statedisplaynameoflastcontact'] = city['state']

	if not found:
		print("Not found")


with open('finalData.json', 'w') as f:
	json.dump(people, f)