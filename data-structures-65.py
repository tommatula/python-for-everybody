# 6.5 Write code using find() and string slicing (see section 6.10) 
# to extract the number at the end of the line below. Convert the 
# extracted value to a floating point number and print it out.

text = "X-DSPAM-Confidence:    0.8475"
# find the string that starts at "0" to end
num = text[text.find("0"):] 
# change num to floating point and print
print(float(num))
