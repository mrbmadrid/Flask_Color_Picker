#turns a dictionary into a list of tuples

def toTuple(dict):
	list = []
	for element in dict:
		list.append((element,dict[element]))
	print list