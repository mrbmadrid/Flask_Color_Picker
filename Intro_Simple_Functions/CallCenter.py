'''
Call center manages calls.

CallCenter.sortByTime() is a bubble sort algorithm

'''


class Call(object):
	def __init__(self, id, caller_name, caller_phone, time, reason):
		self.id = id

		#remove non numeric characters from phone number for easier matching later
		if unicode(caller_phone).isnumeric():
			self.caller_phone = caller_phone
		else:
			self.caller_phone=""
			for c in caller_phone:
				if unicode(c).isnumeric():
					self.caller_phone+=c
		self.caller_name = caller_name
		self.time = time
		self.reason = reason

	def display(self):
		print "Call "+str(self.id)+" info:"
		print self.caller_name
		print self.caller_phone
		print self.time
		print self.reason

class CallCenter(object):
	def __init__(self):
		self.calls = []
		self.queue_size = 0

	def add(self, call):
		if type(call) is Call:
			self.calls.append(call)
			self.queue_size += 1
		return self

	def remove(self):
		if self.queue_size > 0:
			self.calls.pop(0)
			self.queue_size -= 1
		return self

	def info(self):
		for call in self.calls:
			call.display()
		print str(self.queue_size) + " calls in queue"
		return self

	def removeByPhone(self, phone):
		for call in self.calls:
			if call.caller_phone == phone:
				self.calls.remove(call)
				self.queue_size -= 1
		return self

	def sortByTime(self):
		sorted = False
		while not sorted:
			sorted = True
			for count in range (0, self.queue_size):
				while count < self.queue_size-1 and self.calls[count].time > self.calls[count+1].time:
					sorted = False
					temp = self.calls[count+1]
					self.calls[count+1] = self.calls[count]
					self.calls[count] = temp
					print "moved one"
		return self


cc = CallCenter()
cc.add(Call(1, "Brian", "12312-12312", 123, "bad")).add(Call(1, "Brian", 1231212312, 113, "bad")).add(Call(1, "Brian", "12312-12312", 153, "bad")).sortByTime().info().removeByPhone(1231212312).info()