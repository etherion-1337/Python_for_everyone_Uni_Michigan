largest = None
smallest = None

while True:
    num = input("Enter a number: ")
    if num == "done" : break
    try : 
    	ivalue = int(num)
    except :
        print("Invalid input")
        continue
    if smallest is None:
    	smallest = ivalue
    if largest is None:
    	largest = ivalue

    if ivalue <= smallest:
        smallest = ivalue
    if ivalue >= largest:
        largest = ivalue

    #print(num)

print("Maximum is", largest)
print("Minimum is", smallest)