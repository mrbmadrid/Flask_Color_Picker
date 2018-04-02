'''
Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far
'''
import random


def toss5000():
	heads = 0
	tails = 0
	for count in range(1, 5001):
		output = "Attmpt #"+str(count)+": Throwing a coin... It's a "
		if random.random() < 0.5:
			tails += 1
			output+="tail"
		else:
			heads += 1
			output+="head"
		output+="! ... Got "+str(heads)+" head(s) so far and "+str(tails)+" tail(s) so far"
		print output
	print "Ending the program, thank you!"
