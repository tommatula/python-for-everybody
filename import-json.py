import json
import urllib.request, urllib.parse, urllib.error
import ssl

addEmUp = 0
address = input('Enter location: ')
if len(address) < 1:
    address = "http://py4e-data.dr-chuck.net/comments_2009710.json"


handle = urllib.request.urlopen(address)
data = handle.read()

info = json.loads(data)
theList = info['comments']

for item in theList :
    addEmUp = addEmUp+ int(item['count'])
    
print(addEmUp)
