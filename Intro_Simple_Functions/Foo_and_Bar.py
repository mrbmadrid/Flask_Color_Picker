primes = [2]
output = []

def fooBar(floor, ceil):
	base = 2
	while(base*base < floor):
		base += 1

	for count in range(floor, ceil):
		if base*base == count: #Perfect squares
			output.append([count, 'Bar'])
			base += 1
		elif isPrime(count): #primes
			primes.append(count)
			output.append([count, 'Foo'])
		else: #neither
			output.append([count, 'FooBar'])
	for element in output: #Print results as they are created
		print element[0], element[1]

def isPrime(num): #there are much more efficient ways to do this like using a sieve but this way uses no Math library functions
	index = 0
	temp = num
	while(temp > primes[len(primes)-1]*primes[len(primes)-1]):
		temp -= 1
	while temp != num:
		isPrime(temp)
		temp += 1
	while(num > primes[index]*primes[index]):	
		if num%primes[index] == 0:
			return False
		index += 1
	primes.append(num)
	return True


fooBar(100, 100000)