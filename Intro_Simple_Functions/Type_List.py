'''
Assignment: Type List
Write a program that takes a list and prints a message for each element in the list, based on that element's data type.

Your program input will always be a list. For each item in the list, test its data type. If the item is a string, concatenate it onto a new string. If it is a number, add it to a running sum. At the end of your program print the string, the number and an analysis of what the list contains. If it contains only one type, print that type, otherwise, print 'mixed'.

Here are a couple of test cases. Think of some of your own, too. What kind of unexpected input could you get?

#input
l = ['magical unicorns',19,'hello',98.98,'world']
#output
"The list you entered is of mixed type"
"String: magical unicorns hello world"
"Sum: 117.98"
# input
l = [2,3,1,7,4,12]
#output
"The list you entered is of integer type"
"Sum: 29"
# input
l = ['magical','unicorns']
#output
"The list you entered is of string type"
"String: magical unicorns"
'''

l1 = ['magical unicorns',19,'hello',98.98,'world']
l2 = [2,3,1,7,4,12]
l3 = ['magical','unicorns']

def TypeList(list):
	string = ""
	numsum = 0
	unknown = 0

	for element in list:
		if type(element) is int:
			numsum += element
		elif type(element) is str:
			string += " " + element
		else:
			unknown+=1

	if string == "" and numsum == 0 and unknown == 0:
		print "The list you entered is empty"
	elif numsum == 0 and unknown == 0:
		print "The list you entered is of string type"
		print "String:", string
	elif string == "" and unknown == 0:
		print "The list you entered is of integer type"
		print "Sum:", numsum
	else:
		print "The list you entered is of mixed type"

TypeList(l1)
TypeList(l2)
TypeList(l3)


















