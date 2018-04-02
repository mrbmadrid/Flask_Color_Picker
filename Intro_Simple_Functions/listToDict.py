#turns two lists into a dict with the first list as keys the second list as values
#if one list is longer it is used as the key values

def listToDict(list1, list2):
	dict = {}
	if len(list2) > len(list1):
		for count in range(0, len(list1)):
			dict[list2[count]] = list1[count]
	else:
		for count in range(0, len(list1)):
			dict[list1[count]] = list2[count]
	return dict