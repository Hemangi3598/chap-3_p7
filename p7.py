# wapp to find sem of first "n" +ve integers

num = int(input(" enter +ve integer "))
if num < 0:
	print("invalid number")
else:
	sum ,i = 0,1
	while i <= num:
		sum += i
		i += 1
	print(" sum = ", sum)	