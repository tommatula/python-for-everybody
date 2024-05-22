# Use words.txt as the file name
fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print("File not found.")

for fline in fh :
    lineStripped = fline.rstrip()
    print(lineStripped.upper())
    