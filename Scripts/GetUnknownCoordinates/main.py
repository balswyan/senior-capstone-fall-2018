
from collections import OrderedDict
from selenium.webdriver.chrome.options import Options
import re
import selenium
from pyvirtualdisplay import Display
from selenium import webdriver
import json

CHROME_PATH = '/usr/bin/google-chrome'
CHROMEDRIVER_PATH = '/usr/lib/chromium-browser/chromedriver'
WINDOW_SIZE = "1920,1080

chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.binary_location = CHROME_PATH

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH, chrome_options=chrome_options)

with open("final.json") as f:
	people = json.load(f, object_pairs_hook=OrderedDict)

for person in people['results']:

	if person['coordinates']['lat'] == "unknown":
		url = person['link']
		driver.get(url)
		driver.implicitly_wait(.5)
		elems = driver.find_elements_by_xpath("//a[@ng-href]")

		count = 0

		s = ""

		for elem in elems:
			if count == 1:
				break

			if elem.get_attribute("ng-href").startswith('http'):
				s = elem.get_attribute("ng-href")
				count += 1
#				print(s)
				s = str(s)
				a = ""
				b = re.findall(r"[-+]?\d*\.\d+|[-+]?\d+", s)
				c = (a.join(b))
				d = c.split("-", 1)[0] 	# get lat
				e = c.split(d, 1)[1] 	# get lng 

				person['coordinates']['lat'] = d
				person['coordinates']['lng'] = e

			else:
				pass

driver.close()

with open('final2.json', 'w') as f:
	json.dump(people, f)
