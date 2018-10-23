

#All the other code is being imported here:
global inventory
from rooms import *
from items import *
from npc import *
from game_parser import normalise_input as norm


#Assign the global variables for the game
current_room = elevator_corridor
inventory = []



def main():
	#This runs once at the beginning of the game and acts as an intro.
	global current_room
	print('You area a new salesman at the Dunder Mifflen Paper company.')
	print('You well on your way to being the Assistant to the Regional Manager\n')

	#This is the main loop that runs every turn.
	while is_game_still_going():
		print('---------------------------------------------------------------------------------------------------')
		print('Your currently in '+current_room.get_name()) #This shows the room your currently in 
		print(current_room.get_discription())               #along with its description, inventory and characters.
		print(current_room.show_items())

		user_input = str(input('> '))    #This is where the player input is taken in
		instruction = norm(user_input)	 #this runs the input through the parser
		execute(instruction)			 #this then goes to the execute function which is lots of if statments.




def execute(instruction):

	if len(instruction) <= 1 and instruction[0] != 'inventory':		#This tests to make sure the second words was spelled correctly 
		print('I don\'t understand')								#this stops the code from failing if it tries instructinon[1] on a list with 1 element.

	elif instruction[0] == 'go':
		move(instruction[1])							#If the first item in the instruction list is go then it runs
														#the move function with the second item in the list eg a direction
	elif instruction[0] == 'take':
		take_item(instruction[1])						#works the same if the first instruction is take it runs
														#the take function again with the second instruction
	elif instruction[0] == 'drop':
		drop_item(instruction[1])						#Same as the take but with the drop function

	elif instruction[0] == 'look':
		inspect_item(instruction[1])					#This is used to look at the description of an item in your inventory

	elif instruction[0] == 'inventory':
		print('You have in your invenotry',end=' ')
		for item in inventory:							#Prints the contents of your inventory
			print(item.get_name(),end=' ')
		print()								

	elif instruction[0] == 'where':
		if instruction[1].lower() == 'everyone':		#This is the fun one you can say where in 2 ways, either
			for NPC in chars:							#say everyone and that will loop through all the NPC's
				chars[NPC].randomise_movement()			#from the chars dictionary it firsts lets them see if they 
				print(chars[NPC].get_location())		#need to move and then prints their current location.
			print()

		elif instruction[1].lower() in chars:			#This just let you check the location of a specifc character.
			print(chars[instruction[1]].get_location()) 

	elif instruction[0] == 'exit':									#This just lets you exit the infinite loop without having to close the loop.
		doubleCheck = input('Are you sure you want to quit (Y/N)')
		if doubleCheck.upper() == 'Y':								#This just verifies the descion so the player dosen't leave accidentally
			exit()
	else:
		print('I don\'t understand')		#If the instruction isnt blank but is not understood it prints is dosen't understand.

def inspect_item(item):
	if items[item] in inventory:				#This is used to closer inspect an item in your inventory
		print(items[item].get_description())
	else:
		print('That item is not in your inventory')


def move(direction):
	global current_room
	current_room, message = current_room.go(direction)		#This is the move function it runs the room class method that
	if message == False:									#tests to see if the direction the player is trying to go is valid
		print('You can\'t go there...')						#in which case it updates the current_room and if not valid is says you can't move there

def take_item(item):
	if current_room.remove_item(item):										#first runs the room class method to try and remove the item from the rooms
		print('You have succsessfully picked up,',items[item].get_name())   #inventory, that method returns true if it can be removed and triggers 
		inventory.append(items[item])										#adding it to the players inventory.
	else:
		print('You can\'t take that')

def drop_item(item):
	if items[item] in inventory:									#First checks to see if the item is in the player inventory if it is it prints
		print('You have dropped',items[item].get_name())			#that you have dropped the item. Then deletes the item from your inventory
		del(inventory[inventory.index(items[item])])				#and then it runs the room class method add item to add the item to the
		current_room.add_item(item)									#rooms inventory.
	else:															#Otherwise just prints that that item is not in your inventory.	
		print(items[item].get_name(),'is not in your inventory')

def is_game_still_going():				#This is where the win condition will go, all the time that it returns True the game continues.
	return True


if __name__ == '__main__':		#The auto run....
	main()
