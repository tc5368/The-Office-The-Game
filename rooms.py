from items import *

north = 'north';east  = 'east';south = 'south';west  = 'west'

class room():
	def __init__(self,name,description,items):
		self.name = name
		self.exits = []
		self.description = description
		self.inventory = items

	def is_valid_exit(self,direction):
		if direction in self.exits:
			return True
		else:
			return False

	def addExits(self,dictionaryofExits):
		self.exits = dictionaryofExits

	def go(self,direction):
		if self.is_valid_exit(direction): 
			return (self.exits[direction])
		else:
			print('Could not go there...')
			return self

	def get_discription(self):
		return self.description

	def get_name(self):
		return self.name

	def get_exits(self):
		return self.exits

	def show_items(self):
		if len(self.inventory) > 0:
			outString = ''
			for item in self.inventory:
				outString += item.get_name( )+', '
			return str('There is '+outString[:-2]+' here.\n')
		return('')

reception = room('Reception','You can see the whole office from here!',[pen])
elevator_corridor = room('the elevators','The doors open and you walk on the dunder mifflen floor',[])
main_office = room('the Bullpen','This is in the main office area',[computer])
michaels_office = room('Michaels Office','Oh god your in the Bosses Office, good luck',[])
conference_room = room('the Conference Room','You were supposed to be here 5 minutes ago',[])
kitchen_area = room('the Kitchen','Make sure to label your food!, also you see Kevin is making Chilli',[])
annex = room('the Annex','Escape as quickly as possible! This is where Toby is...',[otherExamples])
break_room = room('the Breakroom','Realx and raid the vending machines',[])


reception.addExits({east:main_office,north:michaels_office,west:elevator_corridor})
elevator_corridor.addExits({east:reception})
main_office.addExits({north:conference_room,east:kitchen_area,west:reception})
michaels_office.addExits({south:reception})
conference_room.addExits({south:main_office})
kitchen_area.addExits({east:annex,west:main_office})
annex.addExits({north:break_room,west:kitchen_area})
break_room.addExits({south:break_room})

rooms = {
	'Elevators'        :elevator_corridor,
	'Reception'        :reception,
	'Bullpen'          :main_office,
	'Michaels Office'  :michaels_office, 
	'Conference Room'  :conference_room,
	'Kitchen'          :kitchen_area,
	'The Annex'        :annex,
	'The Breakroom'    :break_room
}