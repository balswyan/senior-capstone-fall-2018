import json

with open('final.json') as f:
    people = json.load(f)

string = ""

for person in people['results']:
    lat = person['coordinates']['lat']
    lng = person['coordinates']['lng']
    person['latitude'] = lat
    person['longitude'] = lng

with open('final2.json', 'w') as f:
    json.dump(people, f)