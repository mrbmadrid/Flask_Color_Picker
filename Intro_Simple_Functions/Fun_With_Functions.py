'''
Odd/Even:
Print 1 to 2000 along with odd or even corresponding to the number
'''

def oddEven():
	for count in range(1, 2001):
		if count%2 == 1:
			print "Number is",count+".","This is an odd number."
		else:
			print "Number is",count+".","This is an even number."

'''
Multiply:
Create a function called 'multiply' that iterates through each value in a list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.

'''

def multiply(list, x):
	newList = []
	for element in list:
		newList.append(element*x)
	return newList

'''
Hacker Challenge:
Write a function that takes the multiply function call as an argument.
Your new function should return the multiplied list as a two-dimensional list.
Each internal list should contain the 1's times the number in the original list.
'''

def tickMarks(list):
	newList = []
	for element in list:
		tempList = []
		for count in range(0, element):
			tempList.append(1)
		newList.append(tempList)
	return newList













