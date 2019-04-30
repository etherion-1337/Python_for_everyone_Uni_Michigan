fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
	if line.startswith("From:") : 
	    line_strip = line.rstrip()
	    #print(line_strip)
	    list_temp = line_strip.split()
	    print(list_temp[1])
	    count = count + 1

#print(count)
print("There were", count, "lines in the file with From as the first word")
