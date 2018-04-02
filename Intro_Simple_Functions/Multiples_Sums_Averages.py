'''Multiples
1. print odd numbers 1 to 1000
2. print multiples of 5 from 5 to 1,000,000
'''

for counter in range(1, 1000):
	if counter%2==1:
		print(counter)
for counter in range(5, 1000000):
	if counter%5==0:
		print(counter)

'''Sum
sum all values in the list a = [1, 2, 5, 10, 255, 3]
'''
a = [1, 2, 5, 10, 255, 3]
sum = 0
for num in a:
	sum += num
print (sum)


'''Average
compute average value of the list a = [1, 2, 5, 10, 255, 3]
'''

a = [1, 2, 5, 10, 255, 3]
sum = 0
for num in a:
	sum += num

print sum/len(a)