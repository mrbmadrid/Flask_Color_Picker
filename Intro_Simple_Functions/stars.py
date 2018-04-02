
#Takes in a list of integers and prints a series of strings of '*' with length equal to the size of each integer
def printStars(list):
	for element in list:
		output = ""
		for count in range(0, element):
			output+="*"
		print output

#Takes in a list of integers and strings and either prints a string of '*' if it is an integer (with length equal ot the size of the integer)
#or if it is a string a new string is created equal to the length of the original string with only the character at the original string's index
#of 0
def printStarsOrFirstLetter(list):
	for element in list:
		output = ""
		if type(element) is str:
			for count in range(0, len(element)):
				output+=element[0].lower()
		else:
			for count in range(0, element):
				output+="*"
		print output
