'''
2d peak finder algorithm

position (i,j) is a peak iff

(i,j) >= (i-1,j)
(i,j) >= (i-1,j)
(i,j) >= (i,j-1)
(i,j) >= (i,j+1)

the = guarantees at least one peak will exist
'''

import numpy as np

a = np.random.randint(100, size=(100,100))

def indexOfMax(list):
	index = 0
	for i in range(0,list.shape[0]):
		if list[i] > list[index]:
			index = i
	return index

def peakFinder(list):
	floor = 0
	ceil = list.shape[0]
	i = ceil/2
	j = 0
	while(True):
		for element in list[i]:
			j = indexOfMax(list[i])
		if(i == 0 and list[i+1][j] <= list[i][j]):
			break
		elif(i == list.shape[0]-1 and list[i-1][j] <= list[i][j]):
			break
		elif not (i == 0 or i == list.shape[0]-1):
			if list[i+1][j] <= list[i][j] and list[i-1][j] <= list[i][j]:
				break
		if list[i-1][j] > list[i][j]:
			ceil = i
			i = int((floor+i)/2)
		else:
			floor = i
			i = int((i+ceil)/2)
	print "Index ("+str(i)+", "+str(j)+") is a peak with a value of "+str(list[i][j])+" and neighboring values of "+str(list[i-1][j])+" "+str(list[i+1][j])+" "+str(list[i][j-1])+" "+str(list[i][j+1])

print a
peakFinder(a)

