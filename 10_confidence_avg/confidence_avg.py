# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)

#for line in fh:
#    if not line.startswith("X-DSPAM-Confidence:") : continue
#    print(line[20:27])
#print("Done")

counter = 0
total = 0.0

for line in fh:
	if not line.startswith("X-DSPAM-Confidence:") : continue
	line_strip = line.rstrip()
	num = float(line_strip[20:])
	total = total + num
	counter = counter + 1

avg = total/counter

print("Average spam confidence:", avg)
