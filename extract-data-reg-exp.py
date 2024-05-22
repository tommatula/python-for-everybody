import re
import os

abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

try:
    handle = open("regex_sum_2009705.txt")
    txt = handle.read()
except:
    print("not found")
     
matches = re.findall('[0-9]+' ,txt)
addEmUp = 0
counter = 0
for i in matches:
    addEmUp = addEmUp + int(i)
    counter = counter + 1

print("Count:",counter,"Sum:",addEmUp)
    
