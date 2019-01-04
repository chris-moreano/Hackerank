# 
#
#
def mylist(arr):
	a = sorted(arr)
	minSum = 0
	maxSum = 0
	for index in range(len(a)):
		if (index == 0):
			minSum = minSum + a[index]
		elif(index == (len(a)-1)):
			maxSum = maxSum + a[index]
		else:
			minSum = minSum + a[index]
			maxSum = maxSum + a[index]
	print(minSum ,"", maxSum)

my_list = [1,2,3,4,5]
mylist(my_list)
