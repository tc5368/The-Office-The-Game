
from rooms import *
from items import *
current_room = elevator_corridor
global inventory

inventory = [pen,computer]

def main():
	global current_room
	print('You area a new salesman at the Dunder Mifflen Paper company.')
	print('You well on your way to being the Assistant to the Regional Manager\n')

	while is_game_still_going():
		print('Your currently in '+current_room.get_name())
		print(current_room.get_discription())
		print(current_room.show_items())
		movement = str(input('> '))

		#This is where the Parser should go...

		if movement in [north,south,east,west]:
			move(movement)
		else:
			print('I don\'t understand')

def move(direction):
	global current_room
	current_room = current_room.go(direction)

def take_item(item):
	if current_room.remove_item(item):
		print('You have succsessfully picked up,',item.get_name())
		inventory.append(item)
	else:
		print('You can\'t take that')

def drop_item(item):
	if item in inventory:
		print('You have dropped',item.get_name())
		del(inventory[inventory.index(item)])
		current_room.add_item(item)

def is_game_still_going():
	return True





if __name__ == '__main__':
	main()
