
import json

with open("missing_people.json") as f:
	people = json.load(f)

with open("us_cities.json") as g:
	cities = json.load(g)

notFoundCount = 0

for person in people['results']:

	found = False

	for city in cities['cities']:

		if (person['cityoflastcontact'] == city['city']) and (person['statedisplaynameoflastcontact'] == city['state_id']):
			found = True
		elif (person['cityoflastcontact'].startswith("unknown")):
			found = True

	if not found:
		print(person['cityoflastcontact'] + ", " + person['countydisplaynameoflastcontact'] + ", " + person['statedisplaynameoflastcontact'])

		notFoundCount = notFoundCount + 1

print("\nNOT FOUND: " + str(notFoundCount))