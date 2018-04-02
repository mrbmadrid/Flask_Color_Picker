def printNames(list):
	for element in list:
		print element["first_name"],element["last_name"]

def printStudentsAndInstructors(obj):
	print "Students"
	count = 1
	for element in obj["Students"]:
		print str(count),element["first_name"],element["last_name"],str(len(element["first_name"])+len(element["last_name"]))
		count+=1
	print "Instructors"
	count = 1
	for element in obj["Instructors"]:
		print str(count),element["first_name"],element["last_name"],str(len(element["first_name"])+len(element["last_name"]))
		count+=1
