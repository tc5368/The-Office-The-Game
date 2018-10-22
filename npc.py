from random import randint as r
from rooms import *

class character():
	def __init__(self, name,starting_location,inventory):	
		self.name = name
		self.current_location = starting_location
		self.inventory = inventory
	def interact(self):
		return None

	def random_direction(self):
		return [north,south,east,west][r(0,3)]

	def get_location(self):
		r = ('staley is currently in '+str(self.current_location).get_name())
		return r

	def randomise_movement(self):
		self.current_location.go(self.random_direction())



stanley = character('stanley',main_office,[])

print(stanley.random_direction())