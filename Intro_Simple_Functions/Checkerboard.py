#print a checkerboard

for x in range (0, 10):
	row = ""
	for y in range (0, 10):
		if x == 0 or y == 0 or x == 9 or y == 9:
			row += '*'
		elif x%2==1:
			if y%2==1:
				row+= '*'
			else:
				row+= " "
		else:
			if y%2==0:
				row+= '*'
			else:
				row+= " "
	print row