

class item():
	def __init__(self, name, description):
		self.name = name
		self.description = description

	def get_name(self):
		return self.name

	def get_discription(self):
		return self.description


pen = item('a Pen','Black Pen, looks to be in good condition')
computer = item('a computer','Very nice computer, but since its an old its probably running vista')
ball = item('a ball','red ball')


items = {'pen':pen,'computer':computer}
