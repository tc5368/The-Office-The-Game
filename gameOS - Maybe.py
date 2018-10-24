

#All the other code is being imported here:
global inventory
from rooms import *
from items import *
from npc import *
from game_parser import normalise_input as norm
import os

#Assign the global variables for the game
current_room = elevator_corridor
inventory = []


def main():
	#This runs once at the beginning of the game and acts as an intro.
	global current_room
	print('You are a new salesman at the Dunder Mifflen Paper company.')
	print('You well on your way to being the Assistant to the Regional Manager\n')

	#This is the main loop that runs every turn.
	while is_game_still_going():

		print('-------------------------------------------------------------------------------------------------')
		print('Your currently in '+current_room.get_name()) #This shows the room your currently in 
		print(current_room.get_discription())               #along with its description, inventory and characters.

		print(who_is_here())

		print(current_room.show_items())

		user_input = str(input('> '))    #This is where the player input is taken in
		instruction = norm(user_input)	 #this runs the input through the parser
		move_NPC()
		execute(instruction)			 #this then goes to the execute function which is lots of if statments.
	print('You Win !!')

def move_NPC():
	for char in chars:
		chars[char].randomise_movement()

def execute(instruction):
	if len(instruction) == 0:
		os.system("cls")
		print('I don\'t understand')

	elif len(instruction) == 1 and instruction[0] not in  ['inventory','exit']:		#This tests to make sure the second words was spelled correctly 
		os.system("cls")
		print('I don\'t understand')												#this stops the code from failing if it tries instructinon[1] on a list with 1 element.

	elif instruction[0] == 'go':
		os.system("cls")
		move(instruction[1])							#If the first item in the instruction list is go then it runs
														#the move function with the second item in the list eg a direction
	elif instruction[0] == 'take':
		os.system("cls")
		take_item(instruction[1])						#works the same if the first instruction is take it runs
														#the take function again with the second instruction
	elif instruction[0] == 'drop':
		os.system("cls")
		drop_item(instruction[1])						#Same as the take but with the drop function

	elif instruction[0] == 'look':
		os.system("cls")
		inspect_item(instruction[1])					#This is used to look at the description of an item in your inventory


	elif instruction[0] == 'give':
		os.system("cls")
		if len(instruction) < 3:
			print('I don\'t understand')
		else:
			give(instruction[1],instruction[2])

	elif instruction[0] == 'inventory':
		os.system("cls")
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
		os.system("cls")
		doubleCheck = input('Are you sure you want to quit (Y/N)')
		if doubleCheck.upper() == 'Y':								#This just verifies the descion so the player dosen't leave accidentally
			exit()
	else:
		os.system("cls")
		print('I don\'t understand')		#If the instruction isnt blank but is not understood it prints is dosen't understand.

def inspect_item(item):
	if items[item] in inventory:				#This is used to closer inspect an item in your inventory
		print(items[item].get_description())
	else:
		print('That item is not in your inventory')


def give(character,item):
	if character not in chars and item not in items and character in items and item in chars:
		temp = character
		character = item 									#One of the things with this command is that it is
		item = temp 										#equally right to say give stanley the pan and
															#give the pen to stanley so have to check which is which
	if character not in chars or item not in items:
		print('I don\'t understand')
	elif items[item] not in inventory:
		print('You don\'t have that item')

	else:
		del(inventory[inventory.index(items[item])])
		chars[character].receive_item(item)
		chars[character].get_inventory()



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
	happy_workers = 0
	for c in chars:
		done = chars[c].is_task_done()
		if done:
			happy_workers += 1
	print(happy_workers)
	if happy_workers == 3:
		return False
	return True


def who_is_here():
	char_string = ''
	for c in chars:
		if chars[c].get_room() == current_room:
			char_string += chars[c].get_name()+' and '
	if char_string != '':
		return char_string[:-4]+'is currently in this room'
	else:
		return 'There is no one here'



def idea():
	stuff_to_save = [current_room,inventory,rooms,items,chars]


if __name__ == '__main__':		#The auto run....
	main()



'''
give NPCS TASK's
THEY ALL WANT A CERTAIN ITEM
THEY NEED DIALOUGE
CHECK TASK COMPLETE
IF 3 NPC Task Complete win game
MAYBE CLS OS if TIME
MAYBE SAVING IF TIME
Add in text stuff

finsih game
'''
