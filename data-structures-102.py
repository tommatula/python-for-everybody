name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
hoursCount = dict()

for eachLine in handle:
    if "From " in eachLine:
        words = eachLine.split()
        time = words[5].split(":")
        hoursCount[time[0]] = hoursCount.get(time[0],0) + 1

lst = list()
for key,value in hoursCount.items():
    newTup = (key,value)
    lst.append(newTup)
lst.sort()

for key,val in lst:
   print(key,val) 
