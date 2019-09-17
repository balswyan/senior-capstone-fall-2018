import urllib2
from cookielib import CookieJar
import os
import re
import time


cookies = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies))
opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 '
                                    '(KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17')]


def image_lookup():
	imagepath ='https://namus.gov/api/CaseSets/NamUs/MissingPersons/Cases/51601/Images/Default/Thumbnail'
	google_path = 'http://images.google.com/searchbyimage?image_url=' + imagepath
	source = opener.open(google_path).read()
	findLinks = re.findall(r'amp;imgrefurl=(.*?)&amp', source)
	for eachThing in findLinks:
		print(eachThing)

image_lookup()