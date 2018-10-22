global inventory
from rooms import *
from items import *
from game_parser import normalise_input as norm

current_room = elevator_corridor

inventory = []

def main():
	global current_room
	print('You area a new salesman at the Dunder Mifflen Paper company.')
	print('You well on your way to being the Assistant to the Regional Manager\n')

	while is_game_still_going():
		print('Your currently in '+current_room.get_name())
		print(current_room.get_discription())
		print(current_room.show_items())
		user_input = str(input('> '))
		instruction = norm(user_input)
		execute(instruction)

def execute(instruction):
	if instruction == []:
		print('I don\'t understand')

	elif instruction[0] == 'go':
		move(instruction[1])

	elif instruction[0] == 'take':
		take_item(instruction[1])

	elif instruction[0] == 'drop':
		drop_item(instruction[1])

	elif instruction[0] in ['i','inventory']:
		print(inventory)

	elif instruction[0] == 'exit':
		doubleCheck = input('Are you sure you want to quit (Y/N)')
		if doubleCheck.upper() == 'Y':
			exit()
	else:
		print('I don\'t understand')


def move(direction):
	global current_room
	current_room = current_room.go(direction)

def take_item(item):
	if current_room.remove_item(item):
		print('You have succsessfully picked up,',items[item].get_name())
		inventory.append(items[item])
	else:
		print('You can\'t take that')

def drop_item(item):
	if items[item] in inventory:
		print('You have dropped',items[item].get_name())
		del(inventory[inventory.index(items[item])])
		current_room.add_item(item)
	else:
		print(items[item].get_name(),'is not in your inventory')

def is_game_still_going():
	return True





if __name__ == '__main__':
	main()
