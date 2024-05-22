fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    lineToCompare = line.split()
    for wordToCompare in lineToCompare:
        if wordToCompare not in lst:
            lst.append(wordToCompare)   
lst.sort()            
print(lst)
