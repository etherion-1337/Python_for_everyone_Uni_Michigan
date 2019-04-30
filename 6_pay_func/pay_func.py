def computepay(h,r):
	money = h*r
	return money

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate:")
r = float(rate)

if h <= 40.0 :
	pay = computepay(h,r)
	print(pay)
else :
	pay = computepay(40.0, r) + computepay(h-40.0, r*1.5)
	print(pay)