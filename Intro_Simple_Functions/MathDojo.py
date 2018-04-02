'''
Adds and subtracts numbers, numbers can be input as nested lists and tuples
'''

class MathDojo(object):
	def __init__(self):
		self.result=0

	def add(self, *arg):
		for e in arg:
			if isinstance(e, (int, long, float, complex)):
				self.result+=e
			elif not e:
				continue
			else:
				for e_n in e:
					self.add(e_n)
		return self

	def subtract(self, *arg):
		for e in arg:
			if isinstance(e, (int, long, float, complex)):
				self.result-=e
			else:
				for e_n in e:
					self.subtract(e_n)
		return self

md = MathDojo()
print md.add([1], 3,4).add([3,5,7,8], [2,4.3,1.25]).subtract(2, (2,3), [1.1,2.3]).result
