# take list types
# add each individual number

def addarrayint(a):
	totalsum = 0
	for number in a:
		totalsum = totalsum + number

	return totalsum


myList = [1000000001,1000000002,1000000003,1000000004,1000000005]
print(addarrayint(myList))