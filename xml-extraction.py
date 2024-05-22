import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

addEmUp = 0
address = input('Enter location: ')
if len(address) < 1:
    address = "http://py4e-data.dr-chuck.net/comments_2009709.xml"


handle = urllib.request.urlopen(address)
data = handle.read()
tree = ET.fromstring(data)
results = tree.findall('comments/comment')

for item in results :
    addEmUp = addEmUp + int(item.find('count').text)
print("Sum:",addEmUp)
    
    


