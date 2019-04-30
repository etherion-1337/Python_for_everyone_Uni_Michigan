# To run this, you can install BeautifulSoup
# https://pypi.python.org/pypi/beautifulsoup4

# Or download the file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('a')

#print(tags[0])
pos = input("Enter position:")
pos = int(pos)
x = tags[pos-1]
url1 = x.get("href", None)

count = input("Enter count:")
count = int(count)

print(url1)

i = 1
while i < count:
	html = urllib.request.urlopen(url1, context=ctx).read()
	soup = BeautifulSoup(html, 'html.parser')
	tags = soup('a')
	print(tags[pos-1].get("href", None))
	url1 = tags[pos-1].get("href", None)
	i = i + 1




#print(x.get("href", None))



#for tag in tags:
    #print(tag.get('href', None))

