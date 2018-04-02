'''
Assignment: Scores and Grades
Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score. Here is the grade table:

Score: 60 - 69; Grade - D
Score: 70 - 79; Grade - C
Score: 80 - 89; Grade - B
Score: 90 - 100; Grade - A

The result should be like this:

Scores and Grades
Score: 98; Your grade is A
End of the program. Bye!
'''

import random
def ScoresAndGrades():
	print "Scores and Grades"
	for count in range(0, 10):
		num = int(random.random() * 41+60)
		output = "Score: "+str(num)+"; Your grade is"
		if num < 70:
			output+=" D"
		elif num < 80:
			output+=" C"
		elif num < 90:
			output+=" B"
		else:
			output+=" A"
		print output
	print "End of the program. Bye!"
