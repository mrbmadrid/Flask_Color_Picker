'''
Assignment: Compare Lists
Write a program that compares two lists and prints a message depending on if the inputs are identical or not.

Your program should be able to accept and compare two lists: list_one and list_two. If both lists are identical print "The lists are the same". If they are not identical print "The lists are not the same." Try the following test cases for lists one and two:

list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]
list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]
list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]
list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']
'''

def compareLists(list1, list2):
	if len(list1) != len(list2):
		return 'The lists are not the same.'
	for count in range(0, len(list1)):
		if list1[count] != list2[count]:
			return 'The lists are not the same.'
	return 'The lists are the same.'



list_one = [1,2,5,6,2]
list_two = [1,2,5,6,2]

print compareLists(list_one, list_two)

list_one = [1,2,5,6,5]
list_two = [1,2,5,6,5,3]

print compareLists(list_one, list_two)

list_one = [1,2,5,6,5,16]
list_two = [1,2,5,6,5]

print compareLists(list_one, list_two)

list_one = ['celery','carrots','bread','milk']
list_two = ['celery','carrots','bread','cream']

print compareLists(list_one, list_two)
