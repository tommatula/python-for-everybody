# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
total = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    strippedString = line.strip("X-DSPAM-Confidence: ")
    total = total + float(strippedString)
    count = count + 1
                                    
print("Average spam confidence:",(total/count))
