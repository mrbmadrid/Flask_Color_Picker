class product(object):
	def __init__(self, price, item_name, weight, brand):
		self.price = price
		self.item_name = item_name
		self.weight = weight
		self.brand = brand
		self.status = "for sale"

	def sell(self):
		self.status = "sold"
		return self

	def addTax(self, tax):
		return self.price*(1.0+tax)

	def returnProduct(self, code):
		if code == 0:
			self.status = "for sale"
		elif code == 1:
			self.status = "defective"
		elif code == 2:
			self.status = "used"
			self.price *= 0.80
		else:
			print "Invalid return code. (0:unopened 1:defective 2:used)"
		return self

	def displayInfo(self):
		print self.item_name
		print "Brand: "+self.brand
		print "Price: $"+str(self.price)
		print "Weighs: "+str(self.weight)
		print "Currently: "+self.status
		return self