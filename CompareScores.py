
# pass two lists as paramaters 
# of 3 elements each, compare and award points 

def compare(comp_a,comp_b):
	apoints = 0;
	bpoints = 0;
	totalpoints = [0,0]
	controlNumber = 0
	for number in comp_a:
		if(comp_a[controlNumber] > comp_b[controlNumber]):
			apoints = apoints + 1
		elif(comp_a[controlNumber] < comp_b[controlNumber]):
			bpoints = bpoints + 1
		controlNumber = controlNumber + 1

	totalpoints[0] = apoints
	totalpoints[1] = bpoints		

	print(totalpoints)

mylistA = [5,6,7]
mylistB = [3,6,10]
compare(mylistA,mylistB)