'''
Assignment: Find Characters
Write a program that takes a list of strings and a string containing a single character, and prints a new list of all the strings containing that character.

Here's an example:

# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output
new_list = ['hello','world']
'''

def findElementsWithChar(list, char):
	result = []
	for element in list:
		if element.find(char) != -1:
			result.append(element)
	return result

word_list = ['hello','world','my','name','is','Anna']
print findElementsWithChar(word_list, 'o')