
import json

import csv

with open('final.json') as f:
    missing_people = json.load(f)

data = missing_people['results']

# open a file for writing

file = open('final.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(file)

count = 0

for person in data:

      if count == 0:

             header = person.keys()

             csvwriter.writerow(header)

             count += 1

      csvwriter.writerow(person.values())

file.close()