
from rooms import *
global current_room


def main():
	current_room = elevator_corridor
	print('You area a new salesman at the Dunder Mifflen Paper company.')
	print('You well on your way to being the Assistant to the Regional Manager\n')

	while True:
		print(current_room['description'])
		break


def move():
	None






if __name__ == '__main__':
	main()