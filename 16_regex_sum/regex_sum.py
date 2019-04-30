import re

fh = open("regex_sum_215842.txt")
numlist = list()

for line in fh:
	line = line.rstrip()
	num_str = re.findall("[0-9]+",line)
	for item in num_str:
		item_int = int(item)
		numlist.append(item_int)

total = sum(numlist)
print(total)
#print(numlist)