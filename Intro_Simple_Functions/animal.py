class animal(object):
	def __init__(self, name, health):
		self.name = name
		self.health = health

	def walk(self):
		self.health-=1
		return self

	def run(self):
		self.health-=5
		return self

	def displayHealth(self):
		print "Health: "+str(self.health)

class dog(animal):
	def __init__(self, name):
		super(dog, self).__init__(name, 150)

	def pet(self):
		self.health+=5
		return self

dog1 = dog("Droopy")

dog1.walk().walk().walk().run().run().pet().displayHealth()

class dragon(animal):
	def __init__(self, name):
		super(dragon, self).__init__(name, 170)

	def fly(self):
		self.health-=10
		return self

	def displayHealth(self):
		super(dragon, self).displayHealth()
		print "I am a dragon"




dragon1 = dragon("Teenie")
dragon1.fly().displayHealth()