name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)
nameDict = dict()

for line in handle:
    if "From " in line:
        words = line.split()
        nameDict[words[1]] = nameDict.get(words[1],0) + 1
        
biggestWord = None
biggestCount = None

for item,countr in nameDict.items():
        if biggestCount == None or countr > biggestCount:
            biggestWord = item
            biggestCount = countr

print(biggestWord,biggestCount)  
