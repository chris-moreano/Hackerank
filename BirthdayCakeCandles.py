def birthdayCakeCandles(ar):
	tempNum = max(ar)
	numberOcurrence = 0

	for index in range(len(ar)):
		if(ar[index] == tempNum):
			numberOcurrence = numberOcurrence + 1

	print(numberOcurrence)

birthdayCakeCandles([3,2,1,3])