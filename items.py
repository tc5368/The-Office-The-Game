

class item():
	def __init__(self, name, description, mass):
		self.name = name
		self.description = description
		self.mass = mass

	def get_name(self):
		return self.name

	def get_mass(self):
		return self.mass

	def get_discription(self):
		return self.description


pen = item('a Pen','Black Pen, looks to be in good condition',0.2)
computer = item('a computer','Very nice computer, but since its an old tv hsow probably running vista',10)
otherExamples = item('name','description',0)