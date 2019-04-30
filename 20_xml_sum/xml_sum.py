import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
data = html.decode()

#print(data)
stuff = ET.fromstring(data)
lst = stuff.findall('.//count')
print('Count:', len(lst))
#print(lst)
total = 0
for item in lst:
    #print('Count:', item.text)
    total = total + int(item.text)

print(total)
