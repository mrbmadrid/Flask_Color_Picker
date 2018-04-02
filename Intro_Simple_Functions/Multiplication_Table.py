#print a checkerboard

for x in range (0, 13):
	row = ""
	for y in range (0, 13):
		if x == 0 or y == 0:
			if not (x==0 and y==0):
				if(x==0):
					row+=str(y)+" "
				else:
					row+=str(x)+" "
		else:
			row+= str(x*y)+" "
	print row