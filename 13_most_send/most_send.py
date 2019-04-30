name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"


handle = open(name)
lst = list()

#read each line, select "From" line, extract 2nd word, make a list 
for line in handle:
	if line.startswith("From") and not line.startswith("From:"):
		line_strip = line.rstrip()
		#print(line_strip)
		list_temp = line_strip.split()
		#print(list_temp[1])
		lst.append(list_temp[1])

#print(lst)

senders = dict()
#dict with histogram
for name in lst:
	senders[name] = senders.get(name,0) + 1

max_name = None
max_time = None

for name, time in senders.items():
	if max_time is None or time > max_time:
		max_name = name
		max_time = time

print(max_name, max_time)
