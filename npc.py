from random import randint as r
from rooms import *

class character():
	def __init__(self, name,starting_location,target,inventory):	
		self.name = name
		self.current_location = starting_location
		self.target = target
		self.inventory = inventory
		self.task = False

	def interact(self):		#Will be used in the future for dialoge
		print(self.get_name()+':  '+first_line_of_dialog[self.get_name()])
		useless_plese_ignore_this_usless_fucking_variable = input('Press any key to continue')
		print(self.get_name()+':  '+second_line_of_dialog[self.get_name()])
		useless_plese_ignore_this_usless_fucking_variable = input('Press any key to continue')



	def is_task_done(self):
		if self.target in self.inventory:
			return True
		else:
			return False

	def receive_item(self,item):
		self.inventory.append(items[item])
		if items[item] != self.target:
			print(self.get_name()+':  '+third_line_of_dialog[self.get_name()])
			self.drop_item(item)
		else:
			print(self.get_name()+':  '+fourth_line_of_dialog[self.get_name()])

	def drop_item(self,item):
		del(self.inventory[self.inventory.index(items[item])])
		self.current_location.add_item(item)

	def get_inventory(self):
		if self.inventory != []:
			print(self.name+' has ',end='')
			for item in self.inventory:							#Prints the contents of your inventory
				print(item.get_name(),end=' ')
			print()	

	def get_room(self):
		return self.current_location

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
		return str(self.name) 			

	def randomise_movement(self):				#Uses the method to get a random direction to try and travel in 
		direction = self.random_direction() 	#If given a direction the NPC uses the same move function as the player
		if direction != None:
			self.current_location, message = self.current_location.go(direction)
												#uses message as beacuse its using the same movement function
												#as the player for the player the message is used to show if movement
												#is not possible, as we don't want the message everytime an NPC
												#can't move we don't use the message variable here but need it there anyway.

#This is where all the Chaarcters are defined, they have a name, starting location and their inventory
stanley = character('Stanley',main_office,crossword_book,[])
jim = character('Jim',reception,computer,[])
pam = character('Pam',reception,teapot,[])
dwight = character('Dwight',kitchen,beet,[])
michael = character('Michael',michaels_office,dundie,[])

#This dictionary is to allow for the string input to be evaluated to an NPC

chars = {'stanley':stanley,'jim':jim,'pam':pam,'dwight':dwight,'michael':michael}


first_line_of_dialog = {
'Jim':'Hi I am Jim, nice to meet you',
'Pam':'Hi I am pam, nice to meet you',
'Dwight':'Beets where is my lucky BEET, MICAHEL JIM TOOK MY BEET',
'Stanley':'Ignores you and searches for his crossword book',
'Michael':'I am Date Mike, Nice to meet me...',
}

second_line_of_dialog = {
'Jim':'Hey can you please do me a favour and help me find my computer',	
'Pam':'Also if you happen to see my teapot could you please let me know!',
'Dwight':'Find the mythical beet and I shall reward you greatly, as the assitant region manager I can do this..',
'Stanley':'Ignores you some more, maybe if you help him find his crossword book he will infally acknowleage you',
'Michael':'Nah but we have fun here, I left my Dundie in the breakroom but i don\'t want to see toby can you go get it for me or your fired',
}

third_line_of_dialog = {
'Jim':'Hi man, sorry that\'s not my computer',	
'Pam':'Oh sorry that\'s not my teapot',
'Dwight':'Why are you handing me this. Does this look like my Beet to you ? MICHAEL the Temp is giving me rubbish!',
'Stanley':'Keeps ignoring you, his only goal is getting back to his crossword to kill time before he can leave',
'Michael':'Urgh NO.'
}

fourth_line_of_dialog = {
'Jim':'Ah thanks man I really appriciate you grabbing my laptop for me!',	
'Pam':'Oh my Teapot, thank you so much, I couldn\'t bear to lose this!',
'Dwight':'You may have a future here after all temp. Now ready for my first elcture in a lond seris of lectures about bear attacks ?',
'Stanley':'OH JOYUS DAY! Stanley Embraces you and thanks you profusley before starting a crosword and forgeting you exsist',
'Michael':'Wow kiss ass much. but seriously thank you. Want to come have dinner with me and Jan ?'
}