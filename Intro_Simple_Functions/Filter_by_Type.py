'''
Test a value by type

A very good explanation of type vs isinstance can be found at https://stackoverflow.com/questions/1549801/what-are-the-differences-between-type-and-isinstance

Integer
If >= 100, print "That's a big number!" elif < 100, print "That's a small number"

String
if len(String) >= 50 print "Long sentence." elif len(String) < 50 print "Short sentence."

List
if len(List) >= 10 print "Big list!" elif len(List) < 10 print "Short list."

Test values:

sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']
'''

sI = 45
mI = 100
bI = 455
eI = 0
spI = -23
sS = "Rubber baby buggy bumpers"
mS = "Experience is simply the name we give our mistakes"
bS = "Tell me and I forget. Teach me and I remember. Involve me and I learn."
eS = ""
aL = [1,7,4,21]
mL = [3,5,7,34,3,2,113,65,8,89]
lL = [4,34,22,68,9,13,3,5,7,9,2,12,45,923]
eL = []
spL = ['name','address','phone number','social security number']

x = [sI, mI, bI, eI, spI, sS, mS, bS, eS, aL, mL, lL, eL, spL]

for element in x:
	if type(element) is int:
		if element >= 100:
			print "That's a big number!" 
		elif element < 100:
			print "That's a small number."
	elif type(element) is str:
		if len(element) >= 50:
			print "Long sentence." 
		elif len(element) < 50:
			print "Short sentence."
	elif type(element) is list:
		if len(element) >= 10:
			print "Big list!"
		elif len(element) < 10:
			print "Short list."

