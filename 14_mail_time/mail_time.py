name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

lst = list()

for line in handle:
	if line.startswith("From") and not line.startswith("From:"):
		line_strip = line.rstrip()
		#print(line_strip)
		pos = line_strip.find(":")
		#print(pos)
		#print(line_strip[pos-2:pos])
		lst.append(line_strip[pos-2:pos])


#print(lst)

hour_count = dict()

for hour in lst:
	hour_count[hour] = hour_count.get(hour,0) + 1

list_sort = list()

for (key,val) in hour_count.items():
	newtup = (key,val)
	list_sort.append(newtup)

list_sort = sorted(list_sort)

for (val, key) in list_sort:
	print(val, key)