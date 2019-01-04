# Given string 12345
# Return the substrings
# 123
# 1,2,3 (Normal loop)
# 12,23
# 123
# 
# return sum

def stringman(tempst):
	mylist = set()
	mystring = str(tempst)
	stradder = mystring[0]
	sumofList = 0
	for index in range(len(mystring)):
		if(index != (len(mystring)-1)):
			temp = mystring[index]+mystring[index+1]
			mylist.add(int(temp))
		if(index > 0):
		# FIRST DIGIT TIME OTHER
			#temp = mystring[0]+mystring[index]
			#mylist.add(int(temp))
		# ADD OTHER POSSITBLE CONVINATIONS

			stradder = stradder + mystring[index]
			mylist.add(int(stradder))
		# SEPARATE ALL DIGITS 	
		mylist.add(int(mystring[index]))
	print(mylist)
	for index in mylist:
		sumofList = sumofList + index

	return sumofList

ms = "123"
print(stringman(ms))

# 1 2 3
# 12 13
# 123
