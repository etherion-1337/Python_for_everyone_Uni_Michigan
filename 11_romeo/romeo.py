fname = input("Enter file name: ")
fh = open(fname)
lst = list()
#for line in fh:
#print(line.rstrip())

for line in fh:
	list_temp = line.split()
	for word in list_temp:
		if word in lst: continue
		lst.append(word)

lst.sort()

print(lst)