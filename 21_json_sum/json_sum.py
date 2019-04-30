import json
import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import xml.etree.ElementTree as ET
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
data = html.decode()

#print(data)

info = json.loads(data)

total = 0

for item in info["comments"]:
    #print("count:", item["count"])
    total = total + int(item["count"])   

print(total)










