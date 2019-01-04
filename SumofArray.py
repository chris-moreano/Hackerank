# Given an array , find the sum of the array 
# input:
# 6
# 2 3 4 5 6 7 

userInput = 0
userArray = []

#userArray = int(input()) 
# takes string of numbers, makes a list of it
userArray = [int(x) for x in input().split()]

totalSum = 0
for numbers in userArray:
	totalSum = totalSum + numbers

print(totalSum)
#print(userArray)
#print(len(userArray))