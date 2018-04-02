class Patient(object):
	def __init__(self, id_num, name, allergies):
		self.id = id_num
		self.name = name
		self.allergies = allergies
		self.bed_num = -1

	def display(self):
		print str(self.id), self.name, self.allergies, str(self.bed_num)


class Hospital(object):
	def __init__(self, name, capacity):
		self.name = name
		self.capacity = capacity
		self.patients = []
		for count in range (0, capacity):
			self.patients.append("empty")

	def admit(self, patient):
		index = 0
		assigned = False
		while(index < self.capacity and not assigned):
			if self.patients[index] == "empty":
				self.patients[index] = patient
				patient.bed_num = index+1
				print "Patient "+str(patient.id)+" " + patient.name+" assigned to bed "+str(index+1)+" in "+self.name
				assigned = True
			index+=1
		if not assigned:
			print self.name + " is full."

	def release(self, name):
		for patient in self.patients:
			if type(patient) is Patient and patient.name.lower() == name.lower():
				patient.bed_num = -1
				print "Releasing "+patient.name
				self.patients.insert(self.patients.index(patient), "empty")
				self.patients.remove(patient)

	def display(self):
		for patient in self.patients:
			if type(patient) is str:
				pass
			else:
				patient.display()

h = Hospital("Tripler", 3)
h.admit(Patient(1, "brian", "mango"))
h.admit(Patient(2, "tim", "none"))
h.admit(Patient(3, "carl", "none"))
h.display()
h.release('Brian')
h.display()











