from product import product

class store(object):
	def __init__(self, address, owner):
		self.address = address
		self.owner = owner
		self.products = []

	def add_product(self, product):
		self.products.append(product)
		return self

	def remove_product(self, name):
		for element in self.products:
			if element.item_name == name:
				self.products.remove(element)
		return self

	def inventory(self):
		for element in self.products:
			element.displayInfo()

store = store("123 fake st", "Kyle")

product1 = product(200, "Thing", 20, "Thing Maker")
product2 = product(300, "Thing1", 15, "Thing Maker")
product3 = product(400, "Thing2", 10, "Thing Maker")
product4 = product(500, "Thing3", 25, "Thing Maker")

store.add_product(product1)
store.add_product(product2)
store.add_product(product3)
store.add_product(product4)

store.inventory()

store.remove_product("Thing2").inventory()

