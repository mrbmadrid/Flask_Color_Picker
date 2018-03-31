#print the position of the first instance of  'day'
words = "It's thanksgiving day. It's my birthday,too!"

print words.index('day')

#find the min and max values
x = [2,54,-2,7,12,98]

print min(x), max(x)

#print the first and last values of the list then create a new list with only those two values
x = ["hello",2,54,-2,7,12,98,"world"]

print x[0], x[len(x)-1]
y = [x[0], x[len(x)-1]]
print y

#sort the list, split the list in half, push the first half list into position 0 of the second half list
x = [19,2,54,-2,7,12,98,32,10,-3,6]

x.sort()
print x
y = x[0:len(x)/2]
z = x[len(x)/2:len(x)]
print y, z
z.insert(0, y)
print z
