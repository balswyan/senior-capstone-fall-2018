import json

with open('final.json') as f:
    people = json.load(f)

string = ""

for person in people['results']:
    string = person["dateoflastcontact"]
    person['year'] = string[0:4]
    person['month'] = string[5:7]
    person['day'] = string[8:10]

with open('final2.json', 'w') as f:
    json.dump(people, f)