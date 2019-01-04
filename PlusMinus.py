# counter the number of positive, negative and zero numbers. divide them by length


def plusMinus(a):
	myList = []
	posNum = 0
	negNum = 0
	zNum = 0
	for index in range(len(a)):
   		if(a[index]>0):
   			posNum = posNum + 1
   		elif(a[index] < 0):
   			negNum = negNum + 1
   		else:
   			zNum = zNum + 1

	print (posNum/len(a))
	print (negNum/len(a))
	print (zNum/len(a))

	#return myList

myList = [-4,3,-9,0,4,1]
plusMinus(myList)


