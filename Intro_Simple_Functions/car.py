class car(object):

	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if self.price > 10000:
			self.tax = 0.15
		else:
			self.tax = 0.12
		self.displayAll()

	def displayAll(self):
		print "Price: $"+str(self.price)
		print "Speed: "+str(self.speed)+"mph"
		print "Mileage: "+str(self.mileage)
		print "Fuel: "+str(self.fuel)
		print "Tax: "+str(self.tax)+"%"
		return self

car1 = car(20000, 0, "Full", 11000)
car2 = car(2000, 67, "Low", 320000)
car3 = car(10000, 120, "Empty", 90000)
car4 = car(15000, 10, "Half full", 112000)
car5 = car(19000, 50, "Half empty", 100)
car6 = car(18999, 90, "Fumes", 123000)

