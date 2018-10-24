from items import *

north = 'north';east  = 'east';south = 'south';west  = 'west'		#This is just for sake of ease.

class room():
	def __init__(self,name,description,items):
		self.name = name
		self.exits = []
		self.description = description
		self.inventory = items

	def is_valid_exit(self,direction):
		if direction in self.exits:									#This just checks to see if the direction given is
			return True												#in the exits dictionary it will then return True or False
		else:
			return False

	def addExits(self,dictionaryofExits):
		self.exits = dictionaryofExits								#Returns the exits dictionary

	def go(self,direction):
		if self.is_valid_exit(direction): 							#This is the main move function, it will check if the
			return self.exits[direction], True						#direction given is a valid exit, if it is then, it
		else:														#will return the room to the side of that exit
			return self, False										#also will return the True or False depending on if
																	#the move was possible.

	def get_discription(self):
		return self.description										#Returns the description of the room

	def get_name(self):
		return self.name 											#Returns the name of the room

	def get_exits(self):
		return self.exits 											#Returns the exits dictionary

	def show_items(self):
		if len(self.inventory) > 0:									#This will print out the items that are located in the room
			outString = ''											#uses a loop to add the list items into a string seperated by a colon
			for i in range(len(self.inventory)):					#and then uses a slice to remove the colon when about to return
				outString += self.inventory[i].get_name( )+', '		#if however if the inventory has 0 elements then is returns a 
			return str('There is '+outString[:-2]+' here.\n')		#blank string instead. This means a blank line if inventory is empty.
		return('')

	def add_item(self,item):
		self.inventory.append(items[item])							#This adds an item into the rooms inventory

	def remove_item(self,item):
		if items[item] in self.inventory:							#This checks to see if a given item is in the room's inventory, if
			del(self.inventory[self.inventory.index(items[item])])	#it's in the inventory then it will remove the item and return True
			return True												#that its been removed or else it will return False
		else:														#to show that the item could not be found in the room inventory.
			return False


#This is where the rooms are assigned 
#Room's ID                Name of the room          Description of the Room                                                Room's Inventory

reception           = room('Reception',           	'You can see the whole office from here!',								[])
elevator_corridor   = room('the elevators',      	'The doors open and you walk on the dunder mifflen floor',				[pen])
main_office         = room('the Bullpen',         	'This is in the main office area',										[computer])
michaels_office     = room('Michaels Office',     	'Oh god your in the Bosses Office, good luck',							[])
conference_room     = room('the Conference Room', 	'You were supposed to be here 5 minutes ago',							[crossword_book])
kitchen             = room('the Kitchen',        	'Make sure to label your food!, also you see Kevin is making Chilli',	[teapot])
annex               = room('the Annex',			  	'Escape as quickly as possible! This is where Toby is...',				[ball])
break_room          = room('the Breakroom',		  	'Realx and raid the vending machines',									[dundie])
accounting          = room('Accounting Department',	'The accountants are here',												[beet])


#because the links between the rooms require the rooms to be initalised before assigment here we have a bank of addExit methods to 
#allow for the exit dictionaries to be added to the already made rooms.

reception.addExits(        	{east:main_office,south:accounting,north:michaels_office,west:elevator_corridor})
elevator_corridor.addExits(	{east:reception})
main_office.addExits(      	{north:conference_room,east:kitchen,west:reception})
michaels_office.addExits(  	{south:reception})
conference_room.addExits(  	{south:main_office})
kitchen.addExits(          	{east:annex,west:main_office})
annex.addExits(            	{north:break_room,west:kitchen})
break_room.addExits(       	{south:break_room})
accounting.addExits(       	{north:reception})

#Here is a dictionary for the rooms to allows for the string to be linked to the room object.
rooms = {
	'Elevators'        :elevator_corridor,
	'Reception'        :reception,
	'Bullpen'          :main_office,
	'Michaels Office'  :michaels_office, 
	'Conference Room'  :conference_room,
	'Kitchen'          :kitchen,
	'The Annex'        :annex,
	'The Breakroom'    :break_room
}