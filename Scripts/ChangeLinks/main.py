import json

with open('data.json') as f:
    people = json.load(f)

for data in people['results']:
    if not data['link'].startswith('http'):
        data['link'] = "https://namus.gov"+data['link']

    if not data['image'].startswith('http'):
        data['image'] = "https://namus.gov"+data['image']

with open('missing_people.json', 'w') as f:
    json.dump(people, f)

