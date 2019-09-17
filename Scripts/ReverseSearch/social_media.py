import urllib2
from cookielib import CookieJar
import os
import re
import time
import json


cookies = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies))
opener.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 '
                                    '(KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17')]
with open("missing_people.json") as f:
	people = json.load(f)

for person in people['results']:
		facebook_profile = 'https://www.facebook.com/search/top/?q='+ person['firstname'] + '%20' + person['lastname']
		facebook_post ='https://www.facebook.com/search/posts/?q='+ person['firstname'] + '%20' + person['lastname']
		facebook_news = 'https://www.facebook.com/search/str/' + person['firstname'] + '%20' + person['lastname'] + '/links-keyword/stories-news-pivot'
		instagram_tags = 'https://www.instagram.com/explore/tags/'+ person['firstname'] + person['lastname']
		twitter_search = 'https://twitter.com/search?q='+ person['firstname'] + '%20' + person['lastname'] + '&src=typd'
		twitter_hashtag = 'https://twitter.com/hashtag/' + person['firstname'] + person['lastname'] '?src=hash'
		print(What ever you want)

