


#This is the item class for the game, Dont worry about this
class item():
	def __init__(self, name, description):
		self.name = name
		self.description = description

	def get_name(self):			
		return self.name 			#This just returns the name of the item

	def get_description(self):
		return self.description		#This just returns the discription of the item

#with the item class all you need to know is that when creating a new item all you need to do is
# do item_name = item('name of the item','description of the item') and then add it to the dictionary at the bottom


#this is where all the items are defined
pen = item('a Pen','Black Pen, looks to be in good condition')
computer = item('a computer','Very nice computer, but since its an old its probably running vista')
ball = item('a ball','red ball')

#this is the dictionary for all the items
items = {'pen':pen,'computer':computer,'ball':ball}
