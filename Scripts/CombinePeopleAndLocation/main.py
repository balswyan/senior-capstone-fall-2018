
import json

with open("missing_people.json") as f:
	people = json.load(f)

with open("us_cities.json") as f:
	cities = json.load(f)


for person in people['results']:

	found = False

	for city in cities['cities']:

		if (person['cityoflastcontact'] == city['city']) and (person['statedisplaynameoflastcontact'] == city['state_id']):
			found = True
			person['coordinates'] = {'lat': city['lat'], 'lng': city['lng']}

		if not found:
			person['coordinates'] = {'lat': 'unknown', 'lng': 'unknown'}


with open('finalData.json', 'w') as f:
	json.dump(people, f)


