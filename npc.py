from random import randint as r
from rooms import *

class character():
	def __init__(self, name,starting_location,inventory):	
		self.name = name
		self.current_location = starting_location
		self.inventory = inventory
		self.task = False

	def interact(self):		#Will be used in the future for dialoge
		return None

	def isTaskDone(self):
		if True:
			return False

	def recieve_item(self,item):
		self.inventory.append(items[item])

	def random_direction(self):
		if r(0,10) > 7:
			return [north,south,east,west][r(0,3)]	#This runs is where the random NPC's decide to move or not,
		else:										#they do an if statment with a random number generator, it has
			return None								#a 3/10 chance to move the character and then tries to go a 
													#random direction, if that direction is valid then the NPC will
													#move to a different room. This is so the NPC's don't move to much.

	def get_location(self):	
		r = (self.get_name()+' is currently in '+str(self.current_location.get_name()))
		return r 				#This function will simply return the name and the location of the given NPC

	def get_name(self):		#This returns the NPC's name
		return self.name 			

	def randomise_movement(self):				#Uses the method to get a random direction to try and travel in 
		direction = self.random_direction() 	#If given a direction the NPC uses the same move function as the player
		if direction != None:
			self.current_location, message = self.current_location.go(direction)
												#uses message as beacuse its using the same movement function
												#as the player for the player the message is used to show if movement
												#is not possible, as we don't want the message everytime an NPC
												#can't move we don't use the message variable here but need it there anyway.

#This is where all the Chaarcters are defined, they have a name, starting location and their inventory
stanley = character('Stanley',main_office,[])
jim = character('Jim',reception,[])
pam = character('Pam',reception,[])
dwight = character('Dwight',kitchen,[])
michael = character('Michael',michaels_office,[])

#This dictionary is to allow for the string input to be evaluated to an NPC
chars = {'stanley':stanley,'jim':jim,'pam':pam,'dwight':dwight,'michael':michael}
